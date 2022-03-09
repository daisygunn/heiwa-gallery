// show toasts
$('.toast').toast('show');

function screenClass() {
    if($(window).innerWidth() < 760) {
        $(".read-more").removeClass("hidden");
        $(".read-less").addClass("hidden");
    } else {
        $(".read-more").addClass("hidden");
        $(".read-less").removeClass("hidden");
    }
}

// Fire.
screenClass();

// And recheck when window gets resized.
$(window).bind('resize',function(){
    screenClass();
});

// navbar drop down toggle 
$(document).ready(function() {
    $(".dropdown-toggle").dropdown();
});


// Footer toggle
function showHours(){
    $("#opening-hours").toggleClass("hidden");
}

function showLocation(){
    $("#location").toggleClass("hidden");
}

$("#show-opening").on('click', function(event) {
    showHours();
})

$("#show-location").on('click', function(event) {
    showLocation();
})


