function suggestions(from, align){
	var suggestion_list = ["Follow social corporates on LinkedIn", "Build New connections on LinkedIn", "Tag new startups on company's posts", "Try to get in touch with all lost out old customers", "Solve issues regarding claim settlements as soon as possible", "Improve automobile insurance policy", "Use ad platform such as Google adsense for company's outreach", "Try to organize workshpos among public awaring them regarding importance of insurance policy", "Be more socially active on facebook and twitter through chatbots", "Provide instant response to customer's queries through AI chatbots"];
	var autoSuggest = "";
	var index =  Math.floor(Math.random()*10);
	type = ['', 'info', 'danger', 'success', 'warning', 'rose', 'primary'];

    color = Math.floor((Math.random() * 6) + 1);

    $.notify({
      icon: "help",
      message: suggestion_list[index]

    }, {
      type: type[color],
      timer: 3000,
      placement: {
        from: from,
        align: align
      }
    });
}
