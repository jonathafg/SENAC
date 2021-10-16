const express = require('express');
const app = express();
const porta = 3000;

app.get('/hello', (req, res) => {
    let nome = "World";
    if(req.query && req.query.nome){
        nome = req.query.nome;
    }
    res.send(`<h1>Hello ${nome}!</h1>`)
    //res.send("<h1>Hello World</h1>");
})

app.get("/produtos", (req, res) => {
    const produto = new Object();
    produto.id = 1,
    produto.nome = "Produto1",
    produto.preco = 30;
    
    res.json(produto);
})

app.listen(porta, () => {
    console.log(`Iniciando servidor na porta ${porta}`)
})