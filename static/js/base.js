/*jshint esversion: 6 */
/*globals $ */

// If window is less than 760 hide footer elements
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

// Footer section toggle toggle
function showHours(){
    $("#opening-hours").toggleClass("hidden");
}

function showLocation(){
    $("#location").toggleClass("hidden");
}

// Function to hide mailchimp messages after 30 seconds
setInterval(() => {
    const errorResponse = document.getElementById("mce-error-response");
    if (errorResponse && errorResponse.style.display === "block") {
        errorResponse.style.display = "none";
        return;
    }
    const successResponse = document.getElementById("mce-success-response");
    if (successResponse && successResponse.style.display === "block") {
        successResponse.style.display = "none";
        return;
    }
}, 30000);

// navbar drop down toggle 
$(document).ready(function() {
    screenClass();

    $(".dropdown-toggle1").on('click', function(event) {
        $(".dropdown-menu1").toggleClass("show");
    });
    $(".dropdown-toggle2").on('click', function(event) {
        $(".dropdown-menu2").toggleClass("show");
    });

    $(".navbar-toggler").on('click', function(event) {
        $(".navbar-collapse").toggleClass("show");
    });

    $("#show-opening").on('click', function(event) {
        showHours();
    });
    
    $("#show-location").on('click', function(event) {
        showLocation();
    });

});

