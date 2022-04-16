// https://datatables.net/examples/index

$(document).ready(function () {
    $('.data_table').DataTable({
            responsive: true,
            scrollY: 800,
            "paging": false,
            columnDefs: [
                { responsivePriority: 1, targets: 0},
                { responsivePriority: 2, targets: -1} 
    ]

            }); $('.dataTables_length').addClass('bs-select');
    });