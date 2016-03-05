function notimsg(){
            $('#noti-msg').delay(500).fadeIn(1000).delay(4000).fadeOut(1000);
}
$(document).ready(function () {
	$("#menuSub").click(function (a){
		a.preventDefault();
		$("#subMenu").toggle();
		$(".cima").toggle();
	});
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
	// $("#enviar1").click(enviar1);
	// $("#enviar2").click(enviar2);
});
function enviarToYou(){
    /* valores */
    var values = [$("#id_toYou-name").val(),$("#id_toYou-phone").val(),$("#id_toYou-mail").val()];
    /* expressoes regulares */
    var expressions = [/^(([a-zA-Z ]|[çáéíóúãẽĩõũàèìòùâêîôû]){1,50})$/,
                                /^(\+[0-9][0-9]) (\([0-9]{2}\))\s([9]{1})?([0-9]{5})-([0-9]{4})$/,
                                /^([\w\-]+\.)*[\w\- ]+@([\w\- ]+\.)+([\w\-]{2,3})$/];
    var names = ["#id_toYou-name","#id_toYou-phone","#id_toYou-mail"];
    var valid = 0;
    /* verifica os arrays se todos estao correspondendo a seus devidos formatos*/
    for (var i = 0; i <values.length; i++) {

       if(expressions[i].test(values[i])){
       		valid++;
           $(names[i]).addClass("valid");
           $(names[i]).removeClass("invalid");
        }else{
            $(names[i]).addClass("invalid");
            $(names[i]).removeClass("valid");
        }
    }

}
function enviarToEJ(){
    /* valores */
    var values = [$("#id_toEJ-phone").val(),$("#id_toEJ-mail").val(),$("#id_toEJ-text").val(),$("#id_toEJ-name").val()];
    /* expressoes regulares */
    var expressions = [/^(\+[0-9][0-9]) (\([0-9]{2}\))\s([9]{1})?([0-9]{5})-([0-9]{4})$/,
                                /^([\w\-]+\.)*[\w\- ]+@([\w\- ]+\.)+([\w\-]{2,3})$/,
                                /^(([a-zA-Z ]|[çáéíóúãẽĩõũàèìòùâêîôû]){1,300})$/,
                                /^(([a-zA-Z ]|[çáéíóúãẽĩõũàèìòùâêîôû]){1,50})$/];
    var names = ["#id_toEJ-phone","#id_toEJ-mail","#id_toEJ-text","#id_toEJ-name"];
    var valid = 0;
    /* verifica os arrays se todos estao correspondendo a seus devidos formatos*/
    for (var i = 0; i <values.length; i++) {

       if(expressions[i].test(values[i])){
       		valid++;
           $(names[i]).addClass("valid");
           $(names[i]).removeClass("invalid");
        }else{
            $(names[i]).addClass("invalid");
            $(names[i]).removeClass("valid");
        }
    }
	if(valid == 4){
		    form.submit();
		}

}
jQuery(function($){
	$("#id_toYou-phone").mask("+99 (99) 99999-9999",{placeholder:" "});
	$("#id_toEJ-phone").mask("+99 (99) 99999-9999",{placeholder:" "});
});

$(function(){
        var url = window.location.pathname,
        urlRegExp = new RegExp(url.replace(/\/$/,'') + "$"); // create regexp to match current url pathname and remove trailing slash if present as it could collide with the link in navigation in case trailing slash wasn't present there
        // now grab every link from the navigation
        $('.nav a').each(function(){
            // and test its normalized href against the url pathname regexp
            if(urlRegExp.test(this.href.replace(/\/$/,''))){
                $(this).addClass('active');
            }
        });

});