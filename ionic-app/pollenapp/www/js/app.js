// Ionic Starter App

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'starter' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'


//angular.module('starter', ['ionic','chart.js'])
angular.module('pollenapp',['ionic','chart.js'])

.controller("ChartController", function($scope,$http) {
  //Chart.defaults.global.elements.line.fill=false;
  function getClimateData(year)
  {
    data = {"data" : []};
    $scope.tempPcpnDates = [];
    $scope.avgtData = [];
    $scope.pcpnData = [];
    var url="http://data.rcc-acis.org/StnData";
    var params = {
      "sid":"usw00026411",
      "sdate":year+"-01-01",
      "edate":year+"12-31",
      "elems":"hdd,pcpn"
    }
    var jsonParams = JSON.stringify(params);
    $http.post(url,jsonParams).
    success(function(data,status,headers,config)
    {
      var avgtData = [];
      var pcpnData = [];
      for(var i=0;i<data["data"].length;i++)
      {
        var curRow = data["data"][i];
        $scope.tempPcpnDates.push(curRow[0]);
        if(curRow[1] != "M")
        {
          avgtData.push(parseFloat(curRow[1]));
        }
        if(curRow[2] != "M" && curRow[2] != "T")
        {
          pcpnData.push(curRow[2]);
        }
      }
      $scope.avgtData.push(avgtData);
      $scope.pcpnData.push(pcpnData);
    }).
    error(function(data,status,headers,config)
    {
      console.log(status);
    });
  }
  $scope.years = [];
  $scope.hddYears = [];
  $scope.currentYear = 2016;
  $scope.currentHDDYear = 2016;
  for(var i=2002;i<2017;i++)
  {
    $scope.years.push(i);
    $scope.hddYears.push(i);
  }
  function getPollenData(year)
  {
  var url_start = 'http://127.0.0.1:8000/pcounts/?year=';
  var url_end = '&max_size=365';
  var url = url_start + year + url_end;
  var pcounts = [];
  $scope.pollenLabels = [];
   $http.get(url).
        then(function(response) {
            //console.log(response.data);
            pcounts = angular.fromJson(response.data);
            var pollenData = {
              birch:[],
              alder:[],
              willow:[],
              poplar_aspen:[],
              spruce:[],
              total_grass:[]
            };
            for(var i=0;i<pcounts.length;i++)
            {
              var jsDate = new Date(pcounts[i].datetime)
              $scope.pollenLabels.push(jsDate.toDateString());
              pollenData.birch.push(pcounts[i].birch);
              pollenData.alder.push(pcounts[i].alder)
              pollenData.willow.push(pcounts[i].willow)
              pollenData.poplar_aspen.push(pcounts[i].poplar_aspen)
              pollenData.spruce.push(pcounts[i].spruce)
              pollenData.total_grass.push(pcounts[i].total_grass)
            }
            $scope.pollenData = [pollenData.birch,pollenData.alder,pollenData.willow,pollenData.poplar_aspen,pollenData.spruce,pollenData.total_grass];
        });
  }
  var dataComplete = getPollenData(2016);
  var climateDataComplete = getClimateData(2016);
  $scope.series = ['Birch',"Alder","Willow","Poplar Aspen","Spruce","Total Grass"];
  $scope.tempPcpnSeries = ['HDD'];
  console.log($scope.series);
  console.log($scope.avgtData);
  $scope.pollenData = [];
  $scope.pollenLabels = [];
  $scope.avgtData = [];
  $scope.pcpnData = [];
  $scope.tempPcpnDates = [];
  $scope.tempPcpnColor = ["#ABCDEF"];
  $scope.options = {
    legend: {display: true},
    scales: {
      xAxes: [
      {
        id: 'x-axis-1',
        maxTicksLimit: 20
      }
      ],

      yAxes: [
      {
        id: 'y-axis-1',
        type:'linear',
        display: true,
        position: 'left'
      }
    ]
    }
  };
  $scope.tempPcpnOptions = {
    legend: {display: true},
    scales: {
      xAxes: [
      {
        id: 'x-axis-climate',
        maxTicksLimit: 20
      }
      ],

      yAxes: [
      {
        id: 'y-axis-climate',
        type:'linear',
        display: true,
        position: 'left'
      }
    ]
    }
  };
  $scope.selectYear = function(year) {
    $scope.currentYear = year;
    getPollenData(year);
  };
  $scope.selectHDDYear = function(year) {
    $scope.currentHDDYear = year;
    getClimateData(year);
  };
})

.run(function($ionicPlatform) {
  $ionicPlatform.ready(function() {
    if(window.cordova && window.cordova.plugins.Keyboard) {
      // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
      // for form inputs)
      cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);

      // Don't remove this line unless you know what you are doing. It stops the viewport
      // from snapping when text inputs are focused. Ionic handles this internally for
      // a much nicer keyboard experience.
      cordova.plugins.Keyboard.disableScroll(true);
    }
    if(window.StatusBar) {
      StatusBar.styleDefault();
    }
  });
})
