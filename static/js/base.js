/*jshint esversion: 6 */
/*globals $ */


// If window is less than 760 
function screenClass() {
    if($(window).innerWidth() < 760) {
        // show icon
        $(".read-more").removeClass("hidden");
        // hide rext
        $(".read-less").addClass("hidden");
        // remove href from 'shop' so it doesn't load when clicked
        $("#navbarDropdown1").removeAttr("href");
        // make dropdown menu icons clickable
        $(".dropdown-toggle1").on('click', function(event) {
            $(".dropdown-menu1").toggleClass("show");
        });
        $(".dropdown-toggle2").on('click', function(event) {
            $(".dropdown-menu2").toggleClass("show");
    });
    } else {
        // add href on larger screen so 'shop' can be clicked
        $("#navbarDropdown1").attr("href", "/products/");
        // hide icon
        $(".read-more").addClass("hidden");
        // show text
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

