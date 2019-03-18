function like_value(){
	var increase = Math.floor(Math.random() * 6);
	like = like + increase;
}
var like = 1500;
like_value();
document.getElementById("likes").innerHtml = like;