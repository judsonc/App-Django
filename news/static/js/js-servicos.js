$(document).ready(function(){
/*	$(".op:first-of-type").addClass("ativa");*/
    $(".op").not(".ativa").click(function(){
        $(".op.ativa").removeClass("ativa");
        $(this).addClass("ativa");
		// if($(this).attr("id") == "consultorias"){
		// 	$("#col02").show();
		// }else{
		// 	$("#col02").hide();
		// }
    // });
});
