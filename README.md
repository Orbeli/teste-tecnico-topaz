# Teste Técnico Topaz
Projeto criado com o objetivo de criar um script, neste caso um endpoint em que é possível agrupar e exibir as principais informações de um usuário do github em JSON e .txt. Apesar de ser um projeto robusto para um objetivo a princípio simples, decidi desenvolver a solução desta forma, pois o projeto possui uma ótima escalabilidade.

---
## Requisitos
1) Python 3.9.x ou superior

---
A instalção pode ser feita com Docker para isso:
1) Criar a *.venv*:
```
    python3 -m venv .venv
```
2) Configura variáveis de ambiente
```
    renomear o arquivo .env.example para .env
```
3) Rodar o comando:
```
    docker-compose up --build
```
4) Pronto, o projeto já está rodando em seu localhost porta 8004, para ver as docs acesse:
```
    http://localhost:8004/docs
```

---
## Start
Após instalado:
1) O projeto pode ser startado novamente através do comando:
```
    docker-compose up
```

---
## Testes
Com o container rodando:
1) utilizar o comando para executar os testes:
```
    docker exec -it teste_topaz pytest -v
```
Para executar os testes unitários do projeto:
1) utilizar o comando para executar os testes:
```
    pytest -v
```

---
## Exemplos de Uso
Exemplos de uso com cURL:
1) Para gerar o relatório de um usuário:
```
    curl --location 'http://localhost:8004/github/get/{USUARIO}'
```
Este endpoint vai retornar um json com os principais dados do usuário e gerar o arquivo {USUARIO}.txt na pasta project\app\github_reports_file
 
---
## Links
[GitHub](https://github.com/Orbeli/flask-api) - GitHub do projeto  

---
## Autor
Gabriel Orbeli Rodrigues Belíssimo

[E-mail](mailto:gabriel.orbeli@gmail.com)
[GitHub](https://github.com/Orbeli)
[Linkedin](https://www.linkedin.com/in/gabriel-orbeli-436815171/)
