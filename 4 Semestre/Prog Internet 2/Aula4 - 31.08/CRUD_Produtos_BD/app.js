const repositorio = require('./repository/produtoRepository')

/* repositorio.inserir({nome:"Prod5", preco:80},
    (err, produto) => {
        if(err) console.log("Erro ao acessar o BD");
        else{
            console.log("Produto add: ");
            console.log(produto);


            
        }
    }); */

repositorio.listar((err, listaProdutos) => {
    if(err) console.log("Erro ao acessar o BD");
    else {
        console.log("Lista de produtos:");
        console.log(listaProdutos)
    }
});

repositorio.buscarPorID(1, (err, produto) => {
    if(err){
        console.log(err);
    }
    else {
        console.log("Produto com id 1: ");
        console.log(produto);
    }
});

repositorio.atualizar(3, {nome:"Prod3", preco:80},
    (err, produto) => {
        if(err) console.log("Erro ao acessar o BD");
        else{
            console.log("Produto Atualizado: ");
            console.log(produto);
        }    
 });

 repositorio.deletar(5, (err, produto) => {
    if(err){
        console.log(err);
    }
    else {
        console.log("Produto removido 5: ");
        console.log(produto);
    }
});