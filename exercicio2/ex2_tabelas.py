import sqlite3

def criar_banco_de_dados():
    # Conectar ao banco de dados (ou criar se não existir)
    conexao = sqlite3.connect("banco_de_dados.db")
    cursor = conexao.cursor()
    
    # Criar tabela de produtos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tbl_produtos (
            produto_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            preco DECIMAL(10, 2) NOT NULL
        )
    ''')
    
    # Criar tabela de fornecedores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tbl_fornecedores (
            fornecedor_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cnpj TEXT UNIQUE NOT NULL,
            cep TEXT NOT NULL,
            estado TEXT NOT NULL,
            cidade TEXT NOT NULL,
            bairro TEXT NOT NULL,
            rua TEXT NOT NULL,
            numero TEXT NOT NULL
        )
    ''')
    
    # Criar tabela de estoque (relacionamento N:M entre produtos e fornecedores)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tbl_estoque (
            estoque_id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto_id INTEGER NOT NULL,
            fornecedor_id INTEGER NOT NULL,
            quantidade INTEGER NOT NULL CHECK(quantidade >= 0),
            FOREIGN KEY (produto_id) REFERENCES tbl_produtos(produto_id),
            FOREIGN KEY (fornecedor_id) REFERENCES tbl_fornecedores(fornecedor_id)
        )
    ''')
    
    # Salvar e fechar conexão
    conexao.commit()
    conexao.close()
    
if __name__ == "__main__":
    criar_banco_de_dados()
    print("Banco de dados SQLite criado com sucesso!")