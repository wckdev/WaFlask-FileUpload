$(function() {
	$('input[type="file"]').change(function(e){
		$('.custom-file-label').html(e.target.files[0].name);
	});
});
