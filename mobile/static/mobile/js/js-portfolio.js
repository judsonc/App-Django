$(document).ready(function () {
	$("#tudo").click(function (a){
		a.preventDefault();
		
		$("img.sites").addClass("mostrarImagem");
		$("div.sites").addClass("col-xs-6");
		$("div.sites").removeClass("ver");
		
		$("img.programas").addClass("mostrarImagem");
		$("div.programas").addClass("col-xs-6");
		$("div.programas").removeClass("ver");
		
		$("img.eventos").addClass("mostrarImagem");
		$("div.eventos").addClass("col-xs-6");
		$("div.eventos").removeClass("ver");
	
	});
	$("#site").click(function (a){
		a.preventDefault();
		
		$("img.sites").addClass("mostrarImagem");
		$("div.sites").addClass("col-xs-6");
		$("div.sites").removeClass("ver");
		
		$("img.programas").removeClass("mostrarImagem");
		$("div.programas").removeClass("col-xs-6");
		$("div.programas").addClass("ver");
		
		$("img.eventos").removeClass("mostrarImagem");
		$("div.eventos").removeClass("col-xs-6");
		$("div.eventos").addClass("ver");
	
	});
	$("#programa").click(function (a){
		a.preventDefault();
		
		$("img.programas").addClass("mostrarImagem");
		$("div.programas").addClass("col-xs-6");
		$("div.programas").removeClass("ver");
		
		$("img.sites").removeClass("mostrarImagem");
		$("div.sites").removeClass("col-xs-6");
		$("div.sites").addClass("ver");
	 	
		$("img.eventos").removeClass("mostrarImagem");
		$("div.eventos").removeClass("col-xs-6");
		$("div.eventos").addClass("ver");
		
	});
	$("#evento").click(function (a){
		a.preventDefault();
		
		$("img.eventos").addClass("mostrarImagem");
		$("div.eventos").addClass("col-xs-6");
		$("div.eventos").removeClass("ver"); 
		
		$("img .sites").removeClass("mostrarImagem");
		$("div .sites").removeClass("col-xs-6");
		$("div .sites").addClass("ver");
		
		$("img.programas").removeClass("mostrarImagem");
		$("div.programas").removeClass("col-xs-6");
		$("div.programas").addClass("ver");
		
	});
	
});