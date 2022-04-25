/*jshint esversion: 6 */
/*globals $ */

// Make date fields date picker
function datePicker() {
    $(".date-picker").datepicker({
        dateFormat: 'dd/mm/yy'
    });
}

$(document).ready(function () {
    datePicker();
    });