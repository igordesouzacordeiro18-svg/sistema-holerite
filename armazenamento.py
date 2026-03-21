import json

ARQUIVO = "funcionarios.json"

def carregar_funcionarios():
    try:
        with open(ARQUIVO, 'r') as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_funcionarios(funcionarios):
    with open(ARQUIVO, 'w') as arquivo:
        json.dump(funcionarios, arquivo, indent=4, ensure_ascii=False)