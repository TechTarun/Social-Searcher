google.charts.load("current", {packages:["corechart"]});
google.charts.setOnLoadCallback(drawChart);

function generate_data(){
  var list = []
  for (var a = 0; a < 7; a++){
    var value = Math.floor(Math.random() * (1000 - 500 + 1) + 500)
    list.push(value)
  }
  return list;
}

function create_date(){
  var date = [];
  var start = Math.floor(Math.random() * 24);
  var end = start + 7;
  for (var a = start; a <= end; a++){
    date.push(`${a}-03-2019`);
  }
  return date;
}

function drawChart() {
  var list = generate_data();
  var date = create_date();
  var data = [['Post on(Last week of Feb 2019)', 'Reach']];
  for (ctr = 0; ctr < 7; ctr++){
    data.push([date[ctr], list[ctr]]);
  }
  var data1 = google.visualization.arrayToDataTable(data);

  var options = {
    title: 'People outreach on page posts',
    pieHole: 0.4,
    is3D: true,
  };

  var chart = new google.visualization.PieChart(document.getElementById('donutchart'));
  chart.draw(data1, options);
}