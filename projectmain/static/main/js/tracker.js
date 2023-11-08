$('#trackerForm').submit(function(event) {
    $('#items').empty();  //Removing everything that is already showing
    $('#amount').empty(); //Removing everything that is already showing
    var formData = {
        'orderId': $('input[name=orderId]').val(),
        'email': $('input[name=email]').val(),
        'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
    };
    $.ajax({
            type: 'POST',
            url: '/main/tracker/',
            data: formData,
            encode: true
    })
    .done(function(data) {
        $('#citems').empty();
        data = JSON.parse(data)
        if (data["status"] == "success") {
            updates = data["updates"];
            for (i = updates.length-1; i >= 0; i--) {
                let text = updates[i]['text'];
                let time = updates[i]['time'];
                mystr = `<li class="list-group-item d-flex justify-content-between align-items-center bg-light">
                ${text}
                <span class="badge badge-primary badge-pill">${time}</span>
            </li>`
                $('#items').append(mystr);
            }

            //Fill in the order details
            cart = JSON.parse(data['itemsJson']);
            let amount = 0;
            for (item in cart) {
                let qty = cart[item][0];
                let name = cart[item][1];
                let price = cart[item][2];
                amount += (price*qty);
                mystr = `<li class="list-group-item d-flex justify-content-between align-items-center bg-light">
                            ${name} (BDT. ${price})
                            <span class="badge badge-primary badge-pill">${qty}</span>
                        </li>`
                $('#citems').append(mystr);
            }
            myStr = `Total: BDT ${amount}`;
            $('#amount').append(myStr);
        } 
        else {
            mystr = `<li class="list-group-item d-flex justify-content-between align-items-center bg-danger text-white">
                Sorry, We are not able to fetch this order id and email. Make sure to type correct order Id and email</li>`
            $('#items').append(mystr);
            $('#citems').append(mystr);
        }

    });
    event.preventDefault();
});