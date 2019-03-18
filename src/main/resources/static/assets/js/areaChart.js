google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart1);

function generate_data(){
  var list = []
  for (var a = 0; a < 7; a++){
    var value = Math.floor(Math.random() * (1000 - 500 + 1) + 500)
    list.push(value)
  }
  return list;
}

var likes = generate_data();
var dislikes = generate_data();
var shares = generate_data();
var days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "frinday", "saturday"];


function drawChart1() {
  var start = Math.floor(Math.random() * 31); 
  date = [start, (start+7)]; 
  var data = [['Date', 'Likes', 'Dislikes', 'Shares']]
  for (var ctr = 0; ctr < 7; ctr++){
    data.push([days[ctr], likes[ctr], dislikes[ctr], shares[ctr]])
  }
  var data1 = google.visualization.arrayToDataTable(data);

  var options1 = {
    title: 'Company Engagements (No. of Followers)',
    hAxis: {title: `Current week(${date[0]} - ${date[1]} March)`,  titleTextStyle: {color: '#333'}},
    vAxis: {minValue: 0, title: 'Followers'},
    isStacked: true
  };

  var chart = new google.visualization.AreaChart(document.getElementById('chart_div'));
  chart.draw(data1, options1);
}