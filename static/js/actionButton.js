window.onload = function () {

    $('.plus').on('click', addToBasket);
    $('.minus').on('click', removeFromBasket);

    function addToBasket() {
        let id = $(this).attr('data-id')
        let val = $(this).attr('value')

        $.ajax({
            url: '/baskets/edit/' + id + '/' + (parseInt(val) + 1) + '/',

            success: function (data) {
                $('.basket_list').html(data.result)}
        }); event.preventDefault();
    }

    function removeFromBasket() {
        $.ajax({
        url: '/baskets/edit/' + $(this).attr('data-id') + '/' + (parseInt($(this).attr('value')) - 1) + '/',
        success: function (data) {
                $('.basket_list').html(data.result)}
        });  event.preventDefault();
    }

}



