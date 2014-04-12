$(document).ready(function(){
	$('.control-update').click(function(){
		track = $.get('/player');
		console.log(track);
	});
	
	$('.control-play').click(function(){
		if(embed_url = $(this).attr('data-embed')) {
				
		} else {
			embed_url = '';
		}
		$.get('/vlc?track=' + embed_url);
	});

	$('.control-pause').click(function(){
		$.get('/stop_vlc');
	});

	
});