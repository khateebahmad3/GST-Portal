var appLogin = angular.module('loginForm', []);

appLogin.controller('validateCtrl', function($scope){
	$scope.user = '';
	$scope.paswrd = '';
});

var appReg = angular.module('registrationsApp', []);

appReg.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
});

appReg.controller('registrationCtrl', function($scope, $http){
	$http.get('/gst/getclients/')
	.then(function(response){
		$scope.names = response.data;
		$scope.process = "registrations";
	});
	$scope.orderByMe = function(x) {
  		if($scope.myOrderBy == undefined || $scope.myOrderBy == x)
  			$scope.myOrderBy = "-" + x;
  		else
  			$scope.myOrderBy = x;
  	};
});

var appRet = angular.module('returnsApp', []);

appRet.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
});

appRet.controller('returnsCtrl', function($scope, $http){
	$http.get('/gst/getreturns/')
	.then(function(response){
		$scope.names = response.data;
		$scope.process = "returns";
	});
	$scope.orderByMe = function(x) {
  		if($scope.myOrderBy == undefined || $scope.myOrderBy == x)
  			$scope.myOrderBy = "-" + x;
  		else
  			$scope.myOrderBy = x;
  	};
});