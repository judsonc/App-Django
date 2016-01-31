$(document).ready(function () {
	$("#menuSub").click(function (a){
		a.preventDefault();
		$("#subMenu").toggle();
		$(".cima").toggle();
	});
});