from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def conectar_bd():
    return sqlite3.connect('db_rede_social.db')


if __name__ == '__main__':
    app.run(debug=True)