(function($) {
  'use strict';
  $(function() {
    var sidebar = $('.sidebar');

    //Add active class to nav-link based on url dynamically
    //Active class can be hard coded directly in html file also as required

    var current = location.pathname//.split("/").slice(-1)[0].replace(/^\/|\/$/g, '');

    $('.nav li a', sidebar).each(function() {
      var $this = $(this);

      if (current === "") {
        //for root url
        if ($this.attr('href').indexOf("index.html") !== -1) {
          $(this).parents('.nav-item').last().addClass('active');
          if ($(this).parents('.sub-menu').length) {
            $(this).closest('.collapse').addClass('show');
            $(this).addClass('active');
          }
        }
      } else {

        //for other url
        if (current.includes('_')) {
          current = current.split('_')[0]
        }
        if ($this.attr('href') == current) {

          $(this).parents('.nav-item').last().addClass('active');
          if ($(this).parents('.sub-menu').length) {
            $(this).closest('.collapse').addClass('show');
            $(this).addClass('active');
          }
        }
      }
    })

    //   var url = window.location;
  
    // var element = $('ul.nav a').filter(function() {
    //     return this.href == url;
    // }).addClass('active').parent();

    // while (true) {
    //     if (element.is('li')) {
    //         element = element.parent().addClass('in').parent();
    //     } else {
    //         break;
    //     }
    // }

    //Close other submenu in sidebar on opening any

    sidebar.on('show.bs.collapse', '.collapse', function() {
      sidebar.find('.collapse.show').collapse('hide');
    });


    //Change sidebar and content-wrapper height
    applyStyles();

    function applyStyles() {
      //Applying perfect scrollbar
      if ($('.scroll-container').length) {
        const ScrollContainer = new PerfectScrollbar('.scroll-container');
      }
    }

    //checkbox and radios
    $(".form-check label,.form-radio label").append('<i class="input-helper"></i>');


    $(".purchace-popup .popup-dismiss").on("click",function(){
      $(".purchace-popup").slideToggle();
    });
  });
})(jQuery);