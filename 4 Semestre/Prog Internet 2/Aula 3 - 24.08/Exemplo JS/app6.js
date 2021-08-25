let listaProdutos = [];

function inserir(produto){
    listaProdutos.push(produto);
}

function atualiza(id, produto){

}

function deletar(id){
    
}

function buscarPorId(id){
    for(let prod of listaProdutos){
        if(prod.id == id){
            return prod;
        }
    }
}

function listar(){
    return listaProdutos;
}

let produto = {id: 1, nome: "Prod1", preco: 10};
inserir(produto);

console.log(listaProdutos);
console.log(buscarPorId(1));