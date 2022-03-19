$(document).ready(function() {
    $(".decrease").on('click', function(event){
        var id=$(this).attr('data-id');
        var product = id.split('_')
        var pk = product[0]
        var value = parseInt(document.getElementById(pk).value, 10);
        value = isNaN(value) ? 0 : value;
        value < 1 ? value = 1 : '';
        value--;
        document.getElementById(pk).value = value;
    });

    $(".increase").on('click', function(event){
        var id=$(this).attr('data-id');
        var product = id.split('_')
        var pk = product[0]
        var value = parseInt(document.getElementById(pk).value, 10);
        value = isNaN(value) ? 0 : value;
        value++;
        document.getElementById(pk).value = value;
    })}
)
