/*jshint esversion: 6 */
/*globals $:false, */

$(document).ready(function() {
    $(".decrease").on('click', function(event){
        var id=$(this).attr('data-id');
        var product = id.split('_');
        var pk = product[0];
        var value = parseInt(document.getElementById(pk).value, 10);
        value = isNaN(value) ? 0 : value;
        value < 1 ? value = 1 : '';
        value--;
        document.getElementById(pk).value = value;
    });

    $(".increase").on('click', function(event){
        var id=$(this).attr('data-id');
        var product = id.split('_');
        var pk = product[0];
        var value = parseInt(document.getElementById(pk).value, 10);
        value = isNaN(value) ? 0 : value;
        value++;
        document.getElementById(pk).value = value;
    });

    // https://datatables.net/examples/index
    $('.data_table').DataTable({
            responsive: true,
            scrollY: 300,
            "paging": false,
            searching: false,
            info: false,
            columnDefs: [
                { responsivePriority: 1, targets: 0},
                { responsivePriority: 10, targets: 1},
                { responsivePriority: 2, targets: 2},
                { responsivePriority: 4, targets: 3},
                { responsivePriority: 5, targets: 5},
                { responsivePriority: 3, targets: -1},

    ]
    });
    $('.dataTables_length').addClass('bs-select');
});