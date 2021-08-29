let listaProdutos = [];

function inserir(produto){
    listaProdutos.push(produto);
}

function atualiza(id, produto){
    for (let prod of listaProdutos){
        if(prod.id == id){
            prod.nome = produto;

            return listaProdutos;
        }
    }
}

function deletar(id){
    for(let prod of listaProdutos){
        if(prod.id == id){
            delete listaProdutos[prod];
        }
    }
    
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
let produto2 = {id: 2, nome: "Prod2", preco: 20};
inserir(produto);
inserir(produto2);

console.log(listaProdutos);
console.log(buscarPorId(1));
console.log(atualiza(1, "prod22"));
console.log(deletar(1));
console.log(listar());