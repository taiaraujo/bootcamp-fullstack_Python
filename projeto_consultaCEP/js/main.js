
function consultaCep(){
    $(".progress_bar").show();
    var cep = document.getElementById("cep").value;
    var url = "https://viacep.com.br/ws/" +cep+ "/json/"
    console.log(cep)
    // biblioteca jquery
    $.ajax({
        url: url,
        type: "GET",
        success: function (response){
            console.log(response);
            // consulta padrão jquery >> requisições ajax
            $("#bairro").html(response.bairro);
            $("#logradouro").html(response.logradouro);
            $("#complemento").html(response.complemento);
            $("#localidade").html(response.localidade);
            $("#uf").html(response.uf);
            $("#title_cep").html("CEP " +response.cep);
            $(".cep").show();
            $(".progress_bar").hide();

            // exemplo de consulta padrão javascript
            // document.getElementById("bairro").innerHTML = response.bairro;
            
            // alert(response.logradouro);
        }
    })
}

// "esconde" todos os elementos da classe cep
$(function(){
    $(".cep").hide();
    $(".progress_bar").hide();
});
