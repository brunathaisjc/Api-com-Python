#  API - é um lugar para disponibilizar recursos e/ou funcionalidades

1. Objetivo - Criar uma api que disponibiliza consulta, criação, edição e exclusão de livros.
2. URL base - localhost:5000
3. Endpoints -
    localhost/livros GET
    localhost/livros/id POST
    localhost/livros/id

Primeiramente:

Usaremos o módulo chamado flask, que é um micro framework em Python para criar APIs e aplicações web.
Depois a classe Flask, usada para criar a aplicação web.
Depois a função jsonify, usada para transformar dicionários (ou listas, etc.) em respostas JSON válidas.
E por último o objeto request, que contém dados da requisição HTTP feita pelo cliente. Por exemplo, para acessar dados de um formulário ou de um corpo JSON.