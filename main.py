# main.py
def saudacao(nome: str) -> str:
    """Retorna uma saudação segura."""
    if not isinstance(nome, str):
        raise TypeError("Nome deve ser uma string")
    return f"Olá, {nome}! Bem-vindo ao sistema."


def calcular_media(notas: list) -> float:
    """Calcula a média de uma lista de notas."""
    if not notas:
        raise ValueError("Lista de notas não pode ser vazia")
    return sum(notas) / len(notas)


import sqlite3

def buscar_usuario_seguro(user_id):
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    # ✅ Query parametrizada — sem risco de SQL Injection
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    return cursor.fetchone()
