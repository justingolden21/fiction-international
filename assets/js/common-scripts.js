$( ()=> {

	$('#menu-btn').click( ()=> {
		if($('#menu-icon').hasClass('fa-bars') ) {
			$('#menu-icon').addClass('fa-times');
			$('#menu-icon').removeClass('fa-bars');
		} else {
			$('#menu-icon').addClass('fa-bars');
			$('#menu-icon').removeClass('fa-times');
		}
	});

	$('.search-icon').click( ()=> {
		$('#search-form').animate({width:'toggle'}, 300);
		$('#search-close').css('display', 'inline');
	});

	$('#search-close').click( ()=> {
		$('#search-form').animate({width:'toggle'}, 0);
		$('#search-close').css('display', '');
	});

});
