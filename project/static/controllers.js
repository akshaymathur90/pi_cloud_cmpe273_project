angular.module('myApp').controller('loginController',
  ['$state','$scope', '$location', 'AuthService',
  function ($state, $scope, $location, AuthService) {

    $scope.login = function () {

      // initial values
      $scope.error = false;
      $scope.disabled = true;

      // call login from service
      AuthService.login($scope.loginForm.email, $scope.loginForm.password)
        // handle success
        .then(function () {
          $location.path('/newapp');
          $state.transitionTo('newapp');
          $scope.disabled = false;
          $scope.loginForm = {};
        })
        // handle error
        .catch(function () {
          $scope.error = true;
          $scope.errorMessage = "Invalid username and/or password";
          $scope.disabled = false;
          $scope.loginForm = {};
        });

    };

}]);

angular.module('myApp').controller('logoutController',
  ['$scope', '$location', 'AuthService',
  function ($scope, $location, AuthService) {
     
    $scope.logout = function () {
      $('body').css("background-image", "url(/static/partials/img/cloud1.jpg)");
      // call logout from service
      AuthService.logout()
        .then(function () {
          $location.path('/login');
        });

    };

}]);

angular.module('myApp').controller('registerController',
  ['$scope', '$location', 'AuthService',
  function ($scope, $location, AuthService) {

    $scope.register = function () {

      // initial values
      $scope.error = false;
      $scope.disabled = true;

      // call register from service
      AuthService.register($scope.registerForm.username,
                           $scope.registerForm.email,
                           $scope.registerForm.password)
        // handle success
        .then(function () {
          $location.path('/login');
          $scope.disabled = false;
          $scope.registerForm = {};
        })
        // handle error
        .catch(function () {
          $scope.error = true;
          $scope.errorMessage = "User Already registered!";
          $scope.disabled = false;
          $scope.registerForm = {};
        });

    };

}]);

angular.module('myApp').controller('appsController', function() {
    /*this.current = 0;
    this.setCurrent = function(newGallery) {
        this.current = newGallery || 0;
    };*/
    $('#bs-sidebar-navbar-collapse-1 ul li').removeClass("active");  // this deactivates the home tab
    $('#bs-sidebar-navbar-collapse-1 ul li').first().addClass("active");
});

angular.module('myApp').controller('mainController',
  ['$scope', 'AuthService',
  function ($scope, AuthService) {

      $scope.sortType     = 'name'; // set the default sort type
      $scope.sortReverse  = false;  // set the default sort order
      $scope.searchFish   = '';     // set the default search/filter term

      AuthService.getUserApps(function(data){
        if(data.status){
          $scope.asushi = data;
        }
        else{
          $scope.asushi = [];
        }
      })
      
      /*$scope.sushi = [
        { name: 'Cali Roll', fish: 'Crab', tastiness: 2 },
        { name: 'Philly', fish: 'Tuna', tastiness: 4 },
        { name: 'Tiger', fish: 'Eel', tastiness: 7 },
        { name: 'Rainbow', fish: 'Variety', tastiness: 6 }
      ];*/
  
}]);



