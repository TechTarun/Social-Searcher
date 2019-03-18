function get_value_tw(){
  document.getElementById('inlineCheckbox1_tw').innerHTML = 1;
}
function get_value_fb(){
  document.getElementById('inlineCheckbox1_fb').innerHTML = 2;
}
function get_value_li(){
  document.getElementById('inlineCheckbox1_li').value = 3;
}
function get_value(){
  console.log(document.getElementById('inlineCheckbox1_tw').value);
  console.log(document.getElementById('inlineCheckbox1_fb').value);
  console.log(document.getElementById('inlineCheckbox1_li').value);
}
