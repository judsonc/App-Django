$(document).ready(function () {
	$("#entrarContatoEject").click(function(a){
		a.preventDefault();
		$("#opcao1").removeClass("ocultar");
		$("#opcao2").addClass("ocultar");

		$("#ejectContato").addClass("exibir");
		$("#voceContato").removeClass("exibir");

	});
	$("#entrarContatoVoce").click(function(a){
		a.preventDefault();
		$("#opcao2").removeClass("ocultar");
		$("#opcao1").addClass("ocultar");

		$("#voceContato").addClass("exibir");
		$("#ejectContato").removeClass("exibir");
	});

});
