$.noConflict( )
jQuery(function($){
    $("#id_data_publicacao").mask("99/99/9999");  
    $("#id_data_expiracao").mask("99/99/9999"); 
    $("#id_inicio_inscricao").mask("99/99/9999");  
    $("#id_fim_inscricao").mask("99/99/9999");  
    $("#id_inicio_bolsa").mask("99/99/9999");  
    $("#id_termino_bolsa").mask("99/99/9999");   
    $("#id_documento_identificacao").mask("99.999.999-9");  
    $("#id_cpf").mask("999.999.999-99");
    $("#id_telefone").mask("(99)9999-9999");
    $("#id_celular").mask("(99)9999-9999");     
    $("#id_hora_inicio").mask("99:99");  
    $("#id_hora_fim").mask("99:99");
    $("#id_agencia").mask("9999-9");  
    $("#id_conta_corrente").mask("99999-9");  
});

function maiuscula(id){
    elemento = document.getElementById(id);
    elemento.value = elemento.value.toUpperCase();
}

function minuscula(id){
    elemento = document.getElementById(id);
    elemento.value = elemento.value.toLowerCase();
}

function num(elemento){
    elemento.value=elemento.value.replace(/\D/g,'');
}  





