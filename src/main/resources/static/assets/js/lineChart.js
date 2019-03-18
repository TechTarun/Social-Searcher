google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart2);

function generate_data(min, max){
  var list = []
  for (var a = 0; a < 12; a++){
    var value = Math.floor(Math.random() * (max - min + 1) + min)
    list.push(value)
  }
  return list;
}

var follow = generate_data(1000, 5000);
var unfollow = generate_data(100, 500);
var month = ['Jan', 'Feb' ,'Mar', 'Apr', 'May', 'June', 'July', 'Aug' ,'Sept', 'Oct' ,'Nov', 'Dec'];

function drawChart2() {
  var data = [['Months', 'No. of follow', 'No. of unfollow']]
  for (var ctr = 0; ctr < 12; ctr++){
    data.push([month[ctr], follow[ctr], unfollow[ctr]]);
  }
  var data2 = google.visualization.arrayToDataTable(data);

var options2 = {
  title: 'Company Performance',
  curveType: 'function',
  legend: { position: 'bottom' }
};

var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));

chart.draw(data2, options2);
}