/*jshint esversion: 6 */
/*globals $ */

$(document).ready(function() {
    // decrease button
    $(".decrease").on('click', function(event){
        // get data id of button clicked and spit at _ to get the product pk
        var id=$(this).attr('data-id');
        var product = id.split('_');
        var pk = product[0];
        // get value of the product quantity box using the pk
        var value = parseInt(document.getElementById(pk).value, 10);
        value = isNaN(value) ? 0 : value;
        // If value is not 0 then reduce by 1
        if(value != 0){
            value--;
        } else {
            // if value is 0 then alert user they cannot reduce
            alert("Number must be bigger than zero.");
            value = value;
        }
        // set the quantity box by the new value
        document.getElementById(pk).value = value;
    });
    // increase button
    $(".increase").on('click', function(event){
         // get data id of button clicked and spit at _ to get the product pk
        var id=$(this).attr('data-id');
        var product = id.split('_');
        var pk = product[0];
        // get value of the product quantity box using the pk
        var value = parseInt(document.getElementById(pk).value, 10);
        value = isNaN(value) ? 0 : value;
        if(value <= 4){
            value++;
        } else {
            // if value is bigger than 4 then alert user they buy more than 5
            alert("You can only purchase a maximum of 5 of a single product");
            value = value;
        }
        document.getElementById(pk).value = value;
    });

    // https://datatables.net/examples/index
    $('.data_table').DataTable({
            responsive: true,
            scrollY: 300,
            "paging": false,
            searching: false,
            info: false,
            // set column priority to hide columns on smaller screen
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