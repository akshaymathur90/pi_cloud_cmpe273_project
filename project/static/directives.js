(function() {
	angular.module('myApp', [])
  .directive("newApp", function() {
        return {
            restrict: 'E',
            templateUrl: "static/partials/newApp.html"
        };
    });
})();  