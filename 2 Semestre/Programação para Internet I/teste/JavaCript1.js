function envia() { 
    if (document.cadastro.nome.value != '' && document.cadastro.endereço.value != '' && document.cadastro.cidade.value != ''  && document.cadastro.estado.value != '' && document.cadastro.usuario.value != '' && document.cadastro.senha.value != '' && document.cadastro.confsenha.value != ''){

        if (document.cadastro.senha.value == document.cadastro.confsenha.value){
            alert('Dados cadastrados com Sucesso! ');
            window.open(URL,"recebeDados")
	    }

        }
        else {
            alert('O Campo senha e a confirmação de senha, não estão iguais!');
        }
    }
    else{
        alert('Existem campos em branco no formulario.');
    }
}