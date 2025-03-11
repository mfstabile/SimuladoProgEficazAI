import sqlite3
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

DB_NAME = "banco_de_dados.db"
VIACEP_URL = "https://viacep.com.br/ws/{}/json/"

def conectar_banco():
    return sqlite3.connect(DB_NAME)

# CRUD Produtos - Item 1:
@app.route("/criarproduto", methods=["POST"])
def cadastrar_produto():
    dados = request.json
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tbl_produtos (nome, descricao, preco) VALUES (?, ?, ?)",
                       (dados["nome"], dados.get("descricao", ""), dados["preco"]))
        conn.commit()
        return jsonify({"produto_id": cursor.lastrowid}), 201

@app.route("/buscaproduto/<int:produto_id>", methods=["GET"])
def obter_produto(produto_id):
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tbl_produtos WHERE produto_id = ?", (produto_id,))
        produto = cursor.fetchone()
        if not produto:
            return jsonify({"erro": "Produto não encontrado"}), 404
        return jsonify({"produto_id": produto[0], "nome": produto[1], "descricao": produto[2], "preco": produto[3]})

@app.route("/listarprodutos", methods=["GET"])
def listar_produtos():
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tbl_produtos")
        produtos = cursor.fetchall()
        return jsonify([{ "produto_id": p[0], "nome": p[1], "descricao": p[2], "preco": p[3]} for p in produtos])

@app.route("/atualizarprodutos/<int:produto_id>", methods=["POST"])
def atualizar_produto(produto_id):
    dados = request.json
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE tbl_produtos SET nome = ?, descricao = ?, preco = ? WHERE produto_id = ?", 
                       (dados["nome"], dados.get("descricao", ""), dados["preco"], produto_id))
        conn.commit()
        return jsonify({"mensagem": "Produto atualizado com sucesso"})

@app.route("/apagarproduto/<int:produto_id>", methods=["GET"])
def excluir_produto(produto_id):
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tbl_produtos WHERE produto_id = ?", (produto_id,))
        conn.commit()
        return jsonify({"mensagem": "Produto excluído com sucesso"})

# CRUD Fornecedores com ViaCEP
@app.route("/fornecedores", methods=["POST"])
def cadastrar_fornecedor():
    # Item 2
    return jsonify({"fornecedor_id": 1}), 201

@app.route("/fornecedores/<int:fornecedor_id>", methods=["GET"])
def obter_fornecedor(fornecedor_id):
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tbl_fornecedores WHERE fornecedor_id = ?", (fornecedor_id,))
        fornecedor = cursor.fetchone()
        if not fornecedor:
            return jsonify({"erro": "Fornecedor não encontrado"}), 404
        return jsonify({"fornecedor_id": fornecedor[0], "nome": fornecedor[1], "cnpj": fornecedor[2], "cep": fornecedor[3], "estado": fornecedor[4], "cidade": fornecedor[5], "bairro": fornecedor[6], "rua": fornecedor[7], "numero": fornecedor[8]})

@app.route("/fornecedores", methods=["GET"])
def listar_fornecedores():
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tbl_fornecedores")
        fornecedores = cursor.fetchall()
        return jsonify([{ "fornecedor_id": f[0], "nome": f[1], "cnpj": f[2], "cep": f[3], "estado": f[4], "cidade": f[5], "bairro": f[6], "rua": f[7], "numero": f[8] } for f in fornecedores])

# CRUD Estoque
@app.route("/estoque", methods=["POST"])
def adicionar_estoque():
    dados = request.json
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tbl_estoque (produto_id, fornecedor_id, quantidade) VALUES (?, ?, ?)",
                       (dados["produto_id"], dados["fornecedor_id"], dados["quantidade"]))
        conn.commit()
        return jsonify({"estoque_id": cursor.lastrowid}), 201

@app.route("/estoque/<int:estoque_id>", methods=["GET"])
def obter_estoque(estoque_id):
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tbl_estoque WHERE estoque_id = ?", (estoque_id,))
        estoque = cursor.fetchone()
        if not estoque:
            return jsonify({"erro": "Entrada de estoque não encontrada"}), 404
        return jsonify({"estoque_id": estoque[0], "produto_id": estoque[1], "fornecedor_id": estoque[2], "quantidade": estoque[3]})

@app.route("/estoque/fornecedor/<int:fornecedor_id>", methods=["GET"])
def listar_estoque_por_fornecedor(fornecedor_id):
    with conectar_banco() as conn:
        cursor = conn.cursor()
        # Item 3
        estoque = []
        return jsonify([{ "estoque_id": e[0], "produto": e[1], "quantidade": e[2]} for e in estoque])

if __name__ == "__main__":
    app.run(debug=True)
