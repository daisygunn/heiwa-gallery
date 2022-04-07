function datePicker() {
    $(".date-picker").datepicker({
        dateFormat: 'dd/mm/yy'
    });
};

$(document).ready(function () {
    datePicker();
    });