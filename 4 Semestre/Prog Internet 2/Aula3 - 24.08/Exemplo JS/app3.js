let lista = []

function inserir(produto){
    lista.push(produto);
}

function listar(){
    return lista;
}

//inserir(produto), listar(), buscarPorId(id), atualizar(id, produto), deletar(id)

inserir({id:1, nome:"produto1", preco:10 });

console.log(listar());