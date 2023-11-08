//function to run the categories owl-carousel
(function ($) {
    $('.owl-carousel').owlCarousel({
        loop: true,
        margin: 20,
        nav: false,
        autoplay: true,
        autoplayTimeout: 5000,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 3
            },
            1000: {
                items: 5
            }
        }
    });
}(owl_carousel_version));


if (localStorage.getItem('cart') == null) {
    var cart = {};
}
else {
    cart = JSON.parse(localStorage.getItem('cart'));
    updateCart(cart);
}

$('.div_pr').on('click', 'button.cart', function () {
    var idstr = this.id.toString();
    if (cart[idstr] != undefined) {
        qty = cart[idstr][0] + 1;

    } else {
        qty = 1;
        name = document.getElementById('name_' + idstr).innerHTML
        price = document.getElementById('price_' + idstr).innerHTML
        cart[idstr] = [qty, name, parseInt(price)];
    }
    updateCart(cart);
    //console.log(cart);
});

$('#popcart').popover();
updatePopover(cart);

function updatePopover(cart) {
    var popStr = "";
    popStr += "<h5> Your Shopping Cart </h5>";
    var i = 1;
    for (var item in cart) {
        popStr += "<b>" + i + "</b>. ";
        popStr += cart[item][1] + "... Qty: " + cart[item][0] + '<br>' + " Price: " + cart[item][2]*cart[item][0] + '<br>';
        i += 1;
    }
    if( Object.keys(cart) != 0 ){
        popStr += "<a href='/main/checkout'><button class='btn btn-success' id ='checkout'>Checkout</button></a> <button class='btn btn-danger' onclick='clearCart()' id ='clearCart'>Clear Cart</button>     "
    }
    document.getElementById('popcart').setAttribute('data-content', popStr);
    $('#popcart').popover('toggle');
}

function clearCart() {
    cart = JSON.parse(localStorage.getItem('cart'));
    for (var item in cart) {
        if(document.getElementById('div_' + item)){
            document.getElementById('div_' + item).innerHTML = '<button id="' + item + '" class="btn btn-warning cart">Add To Cart</button>'
        }
    }
    localStorage.clear();
    cart = {};
    updateCart(cart);
}

function updateCart(cart) {
    var sum = 0;
    for (var item in cart) {
        sum = sum + cart[item][0];
        if (document.getElementById('div_' + item)) {
            document.getElementById('div_' + item).innerHTML = "<button id='minus" + item + "' class='btn btn-warning minus'>-</button> <span id='val" + item + "''>" + cart[item][0] + "</span> <button id='plus" + item + "' class='btn btn-warning plus'> + </button>";
        }
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById('cart').innerHTML = sum;
    updatePopover(cart);
}

// If plus or minus button is clicked, change the cart as well as the display value
$('.div_pr').on("click", "button.minus", function () {
    a = this.id.slice(7,);
    cart['pr' + a][0] = cart['pr' + a][0] - 1;
    cart['pr' + a][0] = Math.max(0, cart['pr' + a][0]);

    if (cart['pr' + a][0] == 0) {
        document.getElementById('div_pr' + a).innerHTML = '<button id="pr' + a + '" class="btn btn-warning cart">Add To Cart</button>';
        delete cart['pr' + a];
    }
    else {
        document.getElementById('valpr' + a).innerHTML = cart['pr' + a][0];
    }
    updateCart(cart);
});
$('.div_pr').on("click", "button.plus", function () {
    a = this.id.slice(6,);
    cart['pr' + a][0] = cart['pr' + a][0] + 1;
    document.getElementById('valpr' + a).innerHTML = cart['pr' + a][0];
    updateCart(cart);
});