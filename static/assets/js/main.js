/*
Template Name: ShopGrids - Bootstrap 5 eCommerce HTML Template.
Author: GrayGrids
*/

(function () {
    //===== Prealoder

    window.onload = function () {
        window.setTimeout(fadeout, 500);
    }

    function fadeout() {
        document.querySelector('.preloader').style.opacity = '0';
        document.querySelector('.preloader').style.display = 'none';
    }


    /*=====================================
    Sticky
    ======================================= */
    window.onscroll = function () {
        var header_navbar = document.querySelector(".navbar-area");
        var sticky = header_navbar.offsetTop;

        // show or hide the back-top-top button
        var backToTo = document.querySelector(".scroll-top");
        if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
            backToTo.style.display = "flex";
        } else {
            backToTo.style.display = "none";
        }
    };

    //===== mobile-menu-btn
    let navbarToggler = document.querySelector(".mobile-menu-btn");
    navbarToggler.addEventListener('click', function () {
        navbarToggler.classList.toggle("active");
    });


})();

window.onload = function () {
    var sorting_menu = document.getElementById('sorting_product')
    var item = document.getElementById('sorting');
    if (item.value == "Low - High Price") {
        sorting_menu.options[1].selected = 'selected';
    } else if (item.value == "High - Low Price") {
        sorting_menu.options[2].selected = 'selected';
    } else if (item.value == "A - Z Order") {
        sorting_menu.options[3].selected = 'selected';
    } else if (item.value == "Z - A Order") {
        sorting_menu.options[4].selected = 'selected';
    }
};
