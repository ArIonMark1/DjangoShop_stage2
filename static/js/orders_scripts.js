window.onload = function () {
    var _quantity, _price, orderitem_num, delta_quantity, orderitem_quantity, delta_cost;
    var quantity_arr = [];
    var price_arr = [];

    // общее количество всех форм в формсетах
    var TOTAL_FORMS = parseInt($('input[name=orderitems-TOTAL_FORMS]').val());
    //
    var order_total_quantity = parseInt($('.order_total_quantity').text()) || 0; // общее количество всех товаров в заказе
    var order_total_cost = parseFloat($('.order_total_cost').text().replace(',', '.')) || 0; // общая цена товаров в заказе

    console.log('order_total_quantity', order_total_quantity);
    console.log('order_total_cost', order_total_cost);

    // берем каждое значение каждогго товара и кладем в соответствующий список
    for (var i = 0; i < TOTAL_FORMS; i++) {
        _quantity = parseInt($('input[name=orderitems-' + i + '-quantity]').val());
        _price = parseFloat($('.orderitems-' + i + '-price').text().replace(',', '.'));
        quantity_arr[i] = _quantity;
        // если нет цены ставим 0
        if (_price) {
            price_arr[i] = _price;
        } else {
            price_arr[i] = 0;
        }
    }

    console.log(quantity_arr);
    console.log(price_arr);

    if (!order_total_quantity) {
        orderSummaryRecalc();
    }

//    обработка события:

    $('.order_form').on('click', 'input[type=number]', function () {
        var target = this;  // идентично: var target = event.target;
        console.log('Target:', target)

        orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-guantity', '')); // берем число которое мы подставили ранее в цикле for
        if (price_arr[orderitem_num]) {
            orderitem_quantity = parseInt(target.value);
            delta_quantity = orderitem_quantity - quantity_arr[orderitem_num];
            quantity_arr[orderitem_num] = orderitem_quantity;
            orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
        }
    });

    $('.order_form').on('click', 'input[type=checkbox]', function () {
        var target = this;
        orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-quantity', ''));

        if (target.checked) {
            delta_quantity = -quantity_arr[orderitem_num];
        } else {
            delta_quantity = quantity_arr[orderitem_num];
        }
        orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
    });
    // ==============================================================
    // удаление пункта заказа
    function deleteOrderItem(row) {
        var target_name = row[0].querySelector('input[type=number]').name;
        orderitem_num = parseInt(target_name.replace('orderitems-', '').replace('-quantity', ''));
        delta_quantity = -quantity_arr[orderitem_num];
        orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
    }

    // ==============================================================

    $('.order_form').on('change', 'select', function () {
        var target = this;

        orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-products', ''));
        var orderitem_product_pk = target.options[target.selectedIndex].value;

        console.log('orderitem_product_pk: ', orderitem_product_pk);

        $.ajax({
            url: '/orders/product/' + orderitem_product_pk + '/price/',
            success: function (data) {

                console.log(data);
                console.log('data price: ', data.price)

                if (data.price) {
                    price_arr[orderitem_num] = parseFloat(data.price);
                    let price_html = `<span>${data.price.toString().replace(',', '.')}</span>руб`;
                    // var price_html = "<span>" + data.price.toString().replace(',', '.') + "</span> руб.";
                    console.log('price_html: ', price_html);

                    var curr_tr = $('.order_form table tbody').find('tr:eq(' + (orderitem_num) + ')');
                    console.log(curr_tr);
                    curr_tr.find('td:eq(2)').html(price_html);
                    orderSummaryRecalc(orderitem_product_pk);
                }
            }
        })

    });

    function orderSummaryRecalc(product_pk) {

        if (product_pk || product_pk[_quantity]) {
            order_total_quantity = null;
            order_total_cost = null;

            for (var i = 0; i < TOTAL_FORMS; i++) {
                order_total_quantity += quantity_arr[i];
                order_total_cost += Number((quantity_arr[i] * price_arr[i]).toFixed(2));
        }
        }

        console.log('quantity_arr: ==>', quantity_arr);
        console.log('price_arr: ==>', price_arr);
        console.log('order_total_cost final: ==> ', order_total_cost);
        console.log('order_total_quantity: ==> ', order_total_quantity);

        $('.order_total_quantity').html(order_total_quantity.toString());
        $('.order_total_cost').html(Number(order_total_cost.toFixed(2)).toString());
    }

// подсчет и вывод в шаблон
    function orderSummaryUpdate(orderitem_price, delta_quantity) {
        delta_cost = orderitem_price * delta_quantity

        order_total_cost = Number((order_total_cost + delta_cost).toFixed(2)) // преобразовали общую стоимость заказа и указали что после запятой будет два знака
        order_total_quantity = order_total_quantity + delta_quantity;


        console.log('order_total_quantity: ==>', order_total_quantity);

        //подставляем новые значения в шаблон страницы
        $('.order_total_quantity').html(order_total_quantity);
        $('.order_total_cost').html(order_total_cost);
    }

    $('.formset_row').formset({
        addText: "добавить товар",
        deleteText: "удалить",
        prefix: "orderitems",
        removed: deleteOrderItem
    });


//     $('order_form').on('click', 'input[type=number]', function () {
//         var target = event.target;
//         orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-quantity', ''));
//         if (price_arr[orderitem_num]) {
//             orderitem_quantity = parseInt(target.value);
//             delta_quantity = orderitem_quantity - quantity_arr[orderitem_num];
//             quantity_arr[orderitem_num] = orderitem_quantity;
//             orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
//         }
//     })
//     // удаление
//     $('.order_form').on('click', 'input[type=checkbox]', function () {
//         var target = event.target;
//         orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-quantity', ''));
//
//         if (target.checked) {
//             delta_quantity = -quantity_arr[orderitem_num];
//         } else {
//             delta_quantity = quantity_arr[orderitem_num];
//         }
//         orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
//     })
//
//     // обновление данных
//     function orderSummaryUpdate(orderitem_price, delta_quantity) {
//         delta_cost = orderitem_price * delta_quantity;
//
//         order_total_cost = Number((order_total_cost + delta_cost).toFixed(2));
//         order_total_quantity = order_total_quantity + delta_quantity;
//
//         $('.order_total_quantity').html(order_total_quantity);
//         $('order_total_cost').html(order_total_cost);
//
//     }
}