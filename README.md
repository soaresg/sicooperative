# Desafio Técnico

## Docker

- Foi criado um docker-compose para a criação automatizada do banco de dados do projeto, para criá-lo deve-se executar o comando

  ```
  docker-compose up -d
  ```

## Inserção de Dados no Database

- Foi criado um arquivo em python para a geração de dados fictícios. Para executar o script deve-se utilizar o seguinte comando no terminal

  ```
  python3 sicooperative/dataInsertion.py
  ```

## ETL de dados

- Para realizar o processo de ETL deste projeto deve-se executar o seguinte comando no terminal

  ```
  python3 main.py
  ```

## Com um prazo maior

- Com um prazo maior para a realização deste desafio refinaria os scripts para ter uma excelência de performance e boas práticas do Python e Spark.

## Dificuldades do projeto

- Algumas dificuldades foram encontradas neste projeto na parte do framework Spark, em sua maior parte na parte de configuração de ambiente para aceitar conexões com o PostgreSQL. Outra dificuldade foi a automatização da criação do banco de dados via Docker.
  - Estes dificuldades apresentadas foram todas resolvidas no decorrer do desenvolvimento deste projeto.
- Houve uma dificuldade na realização dos testes unitários, sendo assim não foi possível criar todos os testes unitários desejados.

## Considerações

### Python

- Escolhido a linguagem Python devido a sua ampla gama de frameworks e packages para auxiliar tanto na população do banco de dados quanto na questão da extração.

### PostgreSQL

- Foi optado por um banco de dados relacional devido ao tipo de dados que seriam armazenados para o desafio, fazendo assim mais coerente utilizar este banco de dados.

### Spark

- Utiliza-se o framework Spark neste caso por se tratar de um framework que possui uma boa compatibilidade com diversas linguagens de programação, neste caso com Python. Como se trata de um sistema open source e um processamento realizado através da memória da máquina, constatou-se que seria ideal para o cenário deste desafio utiliza-lo.
