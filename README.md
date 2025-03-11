# Simulado da Avaliação Intermediária de Programação Eficaz

Insper - 1º Semestre de 2025

## Instruções Gerais

A prova será entregue via Classroom. Não esqueça de fazer commits e push regularmente.

É permitido consultar os materiais da aula, seus projetos, suas APSs e os dominios indicados na sessão "Material permitido para consulta".

É proibida a comunicação entre alunos e entre alunos e pessoas fora da avaliação. Qualquer tentativa de comunicação, seja pessoal ou virtual, será considerada fraude.

É proibido o uso de qualquer site, extensão ou programas que integrem IA ou que auxiliem no desenvolvimento de qualquer aspecto da prova.

Desabilite o Copilot. Caso seja identificado que o Copilot esteve ativo em qualquer momento da prova, será considerado fraude.

**Os professores não ajudarão com configurações de ambiente, Python, problemas de importação, entre outros. Eles poderão apenas esclarecer dúvidas sobre a interpretação do enunciado. A responsabilidade de ter um ambiente funcional para a prova é sua.**

## Exercício 1 - Criação de Base e de API REST com Flask

### Contexto

Você irá desenvolver parte de uma API de uma rede social. Sendo assim, você irá criar as tabelas e implementar as rotas seguindo os requisitos abaixo. Existe um arquivo de testes que deve ser utilizado para testar a API. A questão será corrigida utilizando este mesmo arquivo.

Deverá ser implementado o CRUD de usuarios e de postagens. Um usuário deverá ter nome, email, idade e id de usuário. E uma postagem tem um conteúdo texto, o id do usuário que postou e um id para a postagem em si.

### Parte 1: Banco de Dados

Cria uma base de dados chamada "db_rede_social" no SQLite e as tabelas:

1. **Crie uma tabela `tbl_usuarios`** que deve incluir os seguintes campos:
    - Tabela `tbl_usuarios`:
        - `id` (chave primária, autoincremento)
        - `nome`
        - `email`
        - `idade`

2. **Crie uma tabela `tbl_postagem`** que deve incluir os seguintes campos:
   - Tabela `tbl_postagem`:
     - `id` (chave primária, autoincremento)
     - `conteudo`
     - `id_usuario`


### Parte 2: Criação de um Web Service REST (maturidade 2)

1. **Desenvolva um web service REST em Python usando Flask para os recursos `usuario` e `postagem`:
  - recurso `usuario`
    - Criar um usuário
    - Ler um usuário
    - Ler todos os usuários

  - recurso `postagem`  
   - Criar uma nova postagem
   - Ler uma postagem 
   - Ler todas as postagens
   - Ler todas postagens de um usuário

*Foi fornecido um arquivo de testes e o formato das rotas deve ser exatamente como fornecido. No entanto, lembre-se que os testes de unidade não testam todos os aspectos da API. Faça testes utilizando o Postman quando necessário.*


### Avaliação

- **Item 1:** Criação das tabelas. (até 1,0)
    - Crie um arquivo chamado cria_tabela.py e adicione lá dentro os comandos necessários para criação dessas tabelas no SQLite.
- **Item 2:**  Implementação completa do recurso `usuario` na API REST (Maturidade 2). (até 2,0)
    - Implemente no arquivo app.py.
- **Item 3:**  Implementação completa do recurso `postagem` na API REST (Maturidade 2). (até 2,0)
    - Implemente no arquivo app.py.


## Exercício 2: Cadastro de Produtos e Fornecedores em Estoque com Integração de APIs Externas

### Contexto

Você está desenvolvendo um sistema RESTFul de cadastro para gerenciar o estoque de produtos e seus fornecedores. O sistema precisa registrar informações detalhadas dos produtos e seus fornecedores, incluindo a quantidade disponível em estoque. A relação entre produtos e fornecedores é do tipo N para M, e a tabela de estoque atuará como a tabela relacional que armazena as chaves estrangeiras e a quantidade de cada produto disponível com um determinado fornecedor.

O código de criação da base de dados e das tabelas está na pasta do exercício 2, com o nome: `ex2_tabelas.py`.

O banco de dados contém as seguintes tabelas:

   - **Tabela `tbl_produtos`**:
     - `produto_id` (chave primária, autoincremento)
     - `nome` (string)
     - `descricao` (string)
     - `preco` (decimal)

   - **Tabela `tbl_fornecedores`**:
     - `fornecedor_id` (chave primária, autoincremento)
     - `nome` (string)
     - `cnpj` (string)
     - `cep` (string)
     - `estado` (string)
     - `cidade` (string)
     - `bairro` (string)
     - `rua` (string)
     - `numero` (string)
  
   - **Tabela `tbl_estoque`** (tabela relacional que representa o relacionamento N para M entre Produtos e Fornecedores):
     - `estoque_id` (chave primária, autoincremento)
     - `produto_id`
     - `fornecedor_id`
     - `quantidade` (int)

Uma outra equipe iniciou o desenvolvimento de um web service em Python usando Flask com as seguintes funcionalidades:

#### **CRUD de Produtos:**
- Cadastrar um novo produto.
- Obter os detalhes de um produto específico.
- Listar todos os produtos cadastrados.
- Atualizar um produto existente.
- Excluir um produto.

#### **CRUD de Fornecedores com Enriquecimento de Endereço:**
- O cadastro de um fornecedor deve incluir apenas o CEP no momento da entrada. O web service deve então consultar a API do ViaCEP ([https://viacep.com.br](https://viacep.com.br)) para obter o restante das informações de endereço (estado, cidade, bairro, rua). 
  - Rota esperada: `POST /fornecedores`
  - Tratar possíveis erros como CEP inválido, entradas ausentes ou respostas inesperadas da API do ViaCEP.
  - Rota esperada: `GET /fornecedores/<id_fornecedor>` para obter os detalhes de um fornecedor específico.
  - Rota esperada: `GET /fornecedores` para listar todos os fornecedores.

#### **CRUD do Estoque (associando produtos a fornecedores):**
- Rota esperada: `POST /estoque` para adicionar um produto ao estoque de um fornecedor, incluindo a quantidade disponível.
- Rota esperada: `GET /estoque/<id_estoque>` para obter os detalhes de uma entrada específica no estoque.

#### **Leitura dos Produtos em Estoque de um Fornecedor Específico:**
- Rota esperada: `GET /estoque/fornecedor/<id_fornecedor>` para listar todos os produtos em estoque fornecidos por um fornecedor específico.

### Parte 1: Problemas de implementação

A equipe não terminou de desenvolver o projeto e você recebeu a tarefa de completar o desenvolvimento do web service. Você deve implementar as funcionalidades descritas acima e garantir que todas as rotas estejam funcionando corretamente e no nível 2 da Maturidade de Richardson.

### Parte 2: Testes

Para evitar que novos problemas surjam, você deve criar um arquivo de testes utilizando Pytest para garantir que as rotas funcionem corretamente. Será necessário criar testes para as seguintes rotas:

- Cadastrar um novo produto.
- Obter os detalhes de um produto específico.
- Listar todos os produtos cadastrados.
- Atualizar um produto existente.
- Excluir um produto.
- Cadastrar um novo fornecedor.
- Obter os detalhes de um fornecedor específico.

### Avaliação

- **Item 1:** Desenvolvimento do CRUD completo de produtos (Garantindo um nível de maturidade 2). (1,0 ponto)
- **Item 2:** Desenvolvimento do cadastro de fornecedores com o consumo da API do ViaCEP, incluindo todos os tratamentos de erro. (1,0 pontos)
- **Item 3:** Criação da rota para listar todos os produtos em estoque de um fornecedor específico. (1,0 ponto)
- **Item 4:** Implementação dos testes para as rotas descritas. (2,0 ponto)


## Códigos que não executarem, não serão corrigidos.

## Material permitido para consulta

    - Seus repositórios e repositórios da disciplina (incluindo Projetos e APSs);
    - Site da disciplina;
    - Suas anotações (não podem estar em ferramentas de compartilhamento, como Google Docs);
    - Seus códigos no seu computador;
    - As informações da sessão de Fonte de Informação;

## Fonte de Informação

### Site da diciplina: 
- [https://insper.github.io/ProgramacaoEficaz/](https://insper.github.io/ProgramacaoEficaz/)


### Ajuda com SQL

- [https://www.geeksforgeeks.org/python-sqlite/](https://www.geeksforgeeks.org/python-sqlite/)

### Ajuda com Flask

- Intro: [https://www.tutorialspoint.com/flask/flask_application.htm](https://www.tutorialspoint.com/flask/flask_application.htm)

- Recebendo JSON via requisição: [https://stackabuse.com/how-to-get-and-parse-http-post-body-in-flask-json-and-form-data/](https://stackabuse.com/how-to-get-and-parse-http-post-body-in-flask-json-and-form-data/)

- Variáveis na URL (urls dinâmicas): [https://www.geeksforgeeks.org/generating-dynamic-urls-in-flask/](https://www.geeksforgeeks.org/generating-dynamic-urls-in-flask/)

- Query Parameters: [https://stackabuse.com/get-request-query-parameters-with-flask/](https://stackabuse.com/get-request-query-parameters-with-flask/)

- Documentação oficial: [https://flask.palletsprojects.com/en/3.0.x/](https://flask.palletsprojects.com/en/3.0.x/)

### Ajuda com Testes

- Documentação do Pytest: [https://docs.pytest.org/en/stable/](https://docs.pytest.org/en/stable/)