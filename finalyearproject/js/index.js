//changing topojson to geojson
L.TopoJSON = L.GeoJSON.extend({
    addData: function(jsonData) {
      if (jsonData.type === "Topology") {
        for (let key in jsonData.objects) {
          if (jsonData.objects.hasOwnProperty(key)) {
            let geojson = topojson.feature(jsonData, jsonData.objects[key]);
            L.GeoJSON.prototype.addData.call(this, geojson);
          }
        }
      } else {
        L.GeoJSON.prototype.addData.call(this, jsonData);
      }
    }
  });

let map = L.map("map", { minZoom: 7 }).setView([28.1734922968426, 83.98199462890626],7),topoLayer = new L.TopoJSON();
L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png", {
  attribution:
    '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

let mapIcon = L.icon({
    iconUrl: "https://cdn0.iconfinder.com/data/icons/small-n-flat/24/678111-map-marker-256.png",
    iconSize: [30, 30], // size of the icon
    shadowSize: [50, 64]
});


L.marker([27.19734922968426, 86.8199462890626], { icon: mapIcon })
  .addTo(map)
  .bindPopup("<b>Eatern Development Region!</b><br>Total Affected Areas: 10<br>Highly Affected Place: Dharan")
  .on("mouseover", function() {
    this.openPopup();
  })
  .on("mouseout", function() {
    this.closePopup();
});

L.marker([27.89734922968426, 84.98199462890626], { icon: mapIcon })
  .addTo(map)
  .bindPopup("<b>Central Development Region!</b><br>Capital City, Kathmandu")
  .on("mouseover", function() {
    this.openPopup();
  })
  .on("mouseout", function() {
    this.closePopup();
});

L.marker([28.19734922968426, 83.98199462890626], { icon: mapIcon })
  .addTo(map)
  .bindPopup("<b>Western Development Region!</b>")
  .on("mouseover", function() {
    this.openPopup();
  })
  .on("mouseout", function() {
    this.closePopup();
});


L.marker([28.99734922968426, 82.18199462890626], { icon: mapIcon })
  .addTo(map)
  .bindPopup("<b>Mid Western Development Region!</b>")
  .on("mouseover", function() {
    this.openPopup();
  })
  .on("mouseout", function() {
    this.closePopup();
});

L.marker([29.69734922968426, 80.8199462890626], { icon: mapIcon })
  .addTo(map)
  .bindPopup("<b>Far Western Development Region!</b>")
  .on("mouseover", function() {
    this.openPopup();
  })
  .on("mouseout", function() {
    this.closePopup();
});


//edr map only
// let mymap = L.map("mymap", { minZoom: 7 }).setView([27.3309, 87.0624],7),topoLayer = new L.TopoJSON();
// var mymap = L.map('mapid').setView([27.3309, 87.0624], 13);
// L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png", {
//   attribution:
//     '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
// }).addTo(map);

// let mapIcon = L.icon({
//     iconUrl: "https://cdn0.iconfinder.com/data/icons/small-n-flat/24/678111-map-marker-256.png",
//     iconSize: [30, 30], // size of the icon
//     shadowSize: [50, 64]
// });





var mymap = L.map('mymap').setView([27.3309, 87.0624]);
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    // maxZoom: 18,
    // id: 'mapbox/streets-v11',
    // tileSize: 512,
    // zoomOffset: -1,
    // accessToken: 'your.mapbox.access.token'
    trackResize: false,
}).addTo(mymap);

$(document).ready(function () {
    $('#dataTable').DataTable();
});

(function ($) {
    "use strict"; // Start of use strict
    // Configure tooltips for collapsed side navigation
    $('.navbar-sidenav [data-toggle="tooltip"]').tooltip({
        template: '<div class="tooltip navbar-sidenav-tooltip" role="tooltip" style="pointer-events: none;"><div class="arrow"></div><div class="tooltip-inner"></div></div>'
    })
    // Toggle the side navigation
    $("#sidenavToggler").click(function (e) {
        e.preventDefault();
        $("body").toggleClass("sidenav-toggled");
        $(".navbar-sidenav .nav-link-collapse").addClass("collapsed");
        $(".navbar-sidenav .sidenav-second-level, .navbar-sidenav .sidenav-third-level").removeClass("show");
    });
    // Force the toggled class to be removed when a collapsible nav link is clicked
    $(".navbar-sidenav .nav-link-collapse").click(function (e) {
        e.preventDefault();
        $("body").removeClass("sidenav-toggled");
    });
    // Prevent the content wrapper from scrolling when the fixed side navigation hovered over
    $('body.fixed-nav .navbar-sidenav, body.fixed-nav .sidenav-toggler, body.fixed-nav .navbar-collapse').on('mousewheel DOMMouseScroll', function (e) {
        var e0 = e.originalEvent,
            delta = e0.wheelDelta || -e0.detail;
        this.scrollTop += (delta < 0 ? 1 : -1) * 30;
        e.preventDefault();
    });
    // Scroll to top button appear
    $(document).scroll(function () {
        var scrollDistance = $(this).scrollTop();
        if (scrollDistance > 100) {
            $('.scroll-to-top').fadeIn();
        } else {
            $('.scroll-to-top').fadeOut();
        }
    });
    // Configure tooltips globally
    $('[data-toggle="tooltip"]').tooltip()
    // Smooth scrolling using jQuery easing
    $(document).on('click', 'a.scroll-to-top', function (event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: ($($anchor.attr('href')).offset().top)
        }, 1000, 'easeInOutExpo');
        event.preventDefault();
    });
})(jQuery); // End of use strict
