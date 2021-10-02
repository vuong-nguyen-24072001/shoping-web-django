const allProductApi  = 'http://127.0.0.1:8000/product_api/'

function start(){

    getAllProduct()

}

start()

function getAllProduct(){
    fetch(allProductApi)
        .then((response) => response.json())
        .then((data) => {
            console.log(data)
            handleRenderRecommendProduct(data)
        })
}

function handleRenderRecommendProduct(data){

    let productRecommends = data.filter((product) => product.category == productCurrent)
    const slide2Element = document.querySelector('.slide2')
    const controllSlideElement = document.querySelector('.control-slide')
    if (productRecommends.length >= 8) {
        slide2Element.classList.add('carousel-item')
    }else{
        controllSlideElement.classList.add('opacity-0')
    }
    const productRecommndElements = document.querySelectorAll('.carousel-item .row .col-sm-3')
    console.log(productRecommends.length)
    for (let i = 0; i < productRecommndElements.length; i++){
        if (productRecommends[i] == undefined) break
        productRecommndElements[i].innerHTML = 
            `
            <div class="col-item">
                <div class="info">
                <div class="row">
                    <div class="price ml-2">
                        <p>${productRecommends[i].name}</p>
                        <p class="price-text-color">$${productRecommends[i].price}</p>
                    </div>
                </div>
                <div class="photo">
                    <img src="${productRecommends[i].image_url}" class="img-fluid" alt="a" />
                </div>
                <div class="info">
                    <div class="separator clear-left">
                        <h4 style="display: inline-block; float: left; font-size: 16px; padding: 10px;">sold:</h4>
                        <a href="http://127.0.0.1:8000/product/${productRecommends[i].id}" class="hidden-sm btn float-right"><i class="fa fa-list w-100 p-2"></i></a>
                    </div>
                    <div class="clearfix">
                    </div>
                </div>
            </div>
            `
    }


}