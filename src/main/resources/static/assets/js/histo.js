google.charts.load("current", {packages:["corechart"]});
google.charts.setOnLoadCallback(drawChart);

function generate_data(){
  var list = []
  for (var a = 0; a < 100; a++){
    var value = Math.floor(Math.random() * (45 - 25 + 1) + 25)
    list.push(value)
  }
  return list;
}

var age = generate_data();

function drawChart() {
  var cities = ["Greater Mumbai", "Delhi", "Kolkata", "Bengaluru", "Chennai", "Ahmedabad", "Hyderabad", "Pune", "Kanpur", "Surat", "Jaipur", "Lucknow", "Nagpur", "Indore", "Bhopal", "Ludhiana", "Patna", "Vadodra", "Thane", "Agra", "Kalyan-Dombivali", "Varanasi", "Nashik", "Meerut", "Faridabad", "Haora", "Pimpri Chinchwad", "Allahabad", "Amritsar", "Vishakhapatnam", "Ghazriabad", "Rajkot", "Coimbatore", "Madurai", "Solapur", "Aurangabad", "Ranchi", "Jodhpur", "Gwalior", "Vijaywad", "Chandigarh", "Guwahati", "Hubli-Dharwad", "Tiruchirappalli", "Trivandrum", "Mysore", "Navi Mumbai", "Jalandhar", "Bareilly", "Kota", "Salem", "Aligarh", "Bhubaneshwar", "Moradabad", "Gorakhpur", "Bhiwandi", "Kochi Kerala"];
  var list_data = [["City", "Age"]];
  for (ctr = 0 ; ctr < 100; ctr++){
    list_data.push([cities[ctr], age[ctr]])
  }
  var data = google.visualization.arrayToDataTable(list_data);

  var options = {
    title: "People of various age groups engaged with company's posts",
    legend: { position: 'none' },
    colors: ["#851414"],
  };

  var chart = new google.visualization.Histogram(document.getElementById('chart_div2'));
  chart.draw(data, options);
}