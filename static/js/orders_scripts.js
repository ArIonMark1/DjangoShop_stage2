window.onload = function () {

    var _quantity, _price, orderitem_num, delta_quantity, orderitem_quantity, delta_cost;

    var quantity_arr = [];
    var price_arr = [];

    // общее количество всех форм в формсетах
    var TOTAL_FORMS = parseInt($('input[name=orderitems-TOTAL_FORMS]').val());

    var order_total_quantity = parseInt($('.order_total_quantity').text()) || 0;
    var order_total_cost = parseFloat($('.order_total_cost').text().replace(',', '.')) || 0;

    for (var i = 0; i < TOTAL_FORMS; i++) {
        _quantity = parseInt($('input[name=orderitems-' + i + '-quantity]').val());
        _price = parseFloat($('.orderitems-' + i + '-price').text().replace(',', '.'));

        quantity_arr[i] = _quantity;

        if (_price) {
            price_arr[i] = _price;
        } else {
            price_arr[i] = 0;
        }
    }
    console.log(quantity_arr);
    console.log(price_arr);

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

// подсчет и вывод в шаблон
    function orderSummaryUpdate(orderitem_price, delta_quantity) {
        delta_cost = orderitem_price * delta_quantity

        order_total_cost = Number((order_total_cost + delta_cost).toFixed(2)) // преобразовали общую стоимость заказа и указали что после запятой будет два знака
        order_total_quantity = order_total_quantity + delta_quantity;

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

    function deleteOrderItem(row) {
        var target_name = row[0].querySelector('input[type=number]').name;
        orderitem_num = target_name.replace('orderitems-', '').replace('-quantity', '');
        delta_quantity = -quantity_arr[orderitem_num];
        orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
    }

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