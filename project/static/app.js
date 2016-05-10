var myApp = angular.module('myApp', ['ui.router','ngRoute']);

myApp.config(function($stateProvider, $urlRouterProvider, $routeProvider) {
	$stateProvider
    
        // route to show our basic home (/home)
        .state('newapp', {
            url: 'newapp',
            templateUrl: "static/partials/newApp.html",
            access: {restricted: true}
            /*controller: 'formController'*/
        })
        .state('myapps', {
            url: 'myapps',
            templateUrl: "static/partials/appTable.html",
            access: {restricted: true},
            controller: 'appsController'
        });

    $routeProvider
        .when('/', { templateUrl: 'static/partials/AddApp.html' ,
    				  access: {restricted: true}
    				})
        .when('/login', {
	      templateUrl: 'static/partials/login.html',
	      controller: 'loginController',
	      access: {restricted: false}
	    })
	    .when('/logout', {
	      controller: 'logoutController',
	      access: {restricted: true}
	    })
	    .when('/register', {
	      templateUrl: 'static/partials/register.html',
	      controller: 'registerController',
	      access: {restricted: false}
	    })
	    .when('/one', {
	      template: '<h1>This is page one!</h1>',
	      access: {restricted: true}
	    })
	    .when('/two', {
	      template: '<h1>This is page two!</h1>',
	      access: {restricted: false}
	    })
	    .otherwise({
	      redirectTo: '/'
	    });
});

myApp.run(function ($rootScope, $location, $route, AuthService) {
  $rootScope.$on('$routeChangeStart',
    function (event, next, current) {
      AuthService.getUserStatus()
      .then(function(){
        if (next.access.restricted && !AuthService.isLoggedIn()){
          $location.path('/login');
          $route.reload();
        }
      });
  });
  $rootScope.$on("$stateChangeError", console.log.bind(console));
});
