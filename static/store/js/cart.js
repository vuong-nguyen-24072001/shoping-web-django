var updateCartBtns = document.getElementsByClassName('update-cart')
var totalItemElement = document.querySelector('.total-item')
var totalPriceElement = document.querySelector('.total-price')
var cartItemApi = 'http://127.0.0.1:8000/cart_item_api'

function start(){
    getTotalItem()
}

if (user != 'AnonymousUser'){
    start()
}

function getTotalItem(){
    fetch(cartItemApi)
        .then((response) => response.json())
        .then((data) => {
            let totalCartItem = data.reduce((accumulator, currentValue) => {
                if (currentValue.order == nameCustomer){
                    return accumulator + Number(currentValue.quantity)
                }
                else{
                    return accumulator
                }
            }, 0)
            cartTotalElement = document.getElementById('cart-total')
            cartTotalElement.textContent = totalCartItem
        })
}

console.log(updateCartBtns)
for (let updateCartBtnElement of updateCartBtns){
    updateCartBtnElement.addEventListener('click', function() {
        console.log("vuong")
        let productID = this.dataset.product
        let action = this.dataset.action
        if (user == 'AnonymousUser'){
            console.log('anonymous user')
        }
        else
        {
            console.log("user")
            UpdateUserOrder(productID, action) 
        }
    })
}

function UpdateUserOrder(productID, action){
    // console.log('data sending ...', 'productID:', productID, 'action:', action)
    const url = '/update_item/'
    const dataPost = {'productID': productID, 'action': action}
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(dataPost),
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log(data)
        const cartTotalElement = document.getElementById('cart-total')
        const quantityElement = document.getElementsByClassName('quantity-' + dataPost.productID)[0]
        const priceElement = document.getElementsByClassName('price-' + dataPost.productID)[0]
        const totalElement = document.getElementsByClassName('total-' + dataPost.productID)[0]
        if (dataPost.action == 'add'){
            cartTotalElement.textContent = Number(cartTotalElement.textContent) + 1
            totalElement.textContent = '$' + (Number(quantityElement.textContent)*Number(priceElement.textContent.substring(1))).toFixed(2)
            totalItemElement.textContent =  Number(totalItemElement.textContent) + 1
            totalPriceElement.textContent = (Number(totalPriceElement.textContent) + Number(priceElement.textContent.substring(1))).toFixed(2)
            quantityElement.textContent = Number(quantityElement.textContent) + 1
        }else
        if ((dataPost.action == 'remove') && (Number(quantityElement.textContent) > 0))
        {
            totalItemElement.textContent =  Number(totalItemElement.textContent) - 1
            totalPriceElement.textContent = (Number(totalPriceElement.textContent) - Number(priceElement.textContent.substring(1))).toFixed(2)
            quantityElement.textContent = Number(quantityElement.textContent) - 1
            cartTotalElement.textContent = Number(cartTotalElement.textContent) - 1    
            totalElement.textContent = '$' + (Number(quantityElement.textContent)*Number(priceElement.textContent.substring(1))).toFixed(2)
        }
    })
}
