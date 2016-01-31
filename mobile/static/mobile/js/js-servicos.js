$(document).ready(function(){
/*	$(".op:first-of-type").addClass("ativa");*/

	/*
    $(".op").not(".ativa").click(function(){
        $(".op.ativa").removeClass("ativa");
        $(this).addClass("ativa");
		
		if($(this).attr("id") == "consultorias"){
			$("#col02").show();
		}else{
			$("#col02").hide();
		}
    });
	*/

		$("#sites").click(function (div){
		$(".box2").removeClass("ativado");
		$("#sites .box2").addClass("ativado");
		$("#col02").removeClass("ativado");
	
	});
	$("#consultorias").click(function (div){
		$(".box2").removeClass("ativado");
		$("#consultorias .box2").addClass("ativado");
		$("#col02").addClass("ativado");
		
	
	});
	$("#ambiental").click(function (div){

		$("#ambiental .box22").addClass("ativado");
		$("#inovacao .box22").removeClass("ativado");
	});
	$("#inovacao").click(function (div){
		$("#ambiental .box22").removeClass("ativado");
		$("#inovacao .box22").addClass("ativado");
	});
	$("#programas").click(function (div){
		$(".box2").removeClass("ativado");
		$("#programas .box2").addClass("ativado");
		$("#col02").removeClass("ativado");
	
	});
	
	
	$("#eventos").click(function (div){
		$(".box2").removeClass("ativado");
		$("#eventos .box2").addClass("ativado");
		$("#col02").removeClass("ativado");
	
	});

});
