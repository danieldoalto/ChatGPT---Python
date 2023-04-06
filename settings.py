import json

# Exemplo de dicionário com diferentes tipos de dados
dados = {
    'cnf1':{
    'engine':'text-davinci-003',
    'prompt': 'question',
    'temperature ':0.5,
    'max_tokens':150,
    'top_p':1,
    'frequency_penalty':0,
    'presence_penalty':0.6},
    'cnf2':{
    'engine':'text-davinci-003',
    'prompt': 'question',
    'temperature ':0.5,
    'max_tokens':150,
    'top_p':1,
    'frequency_penalty':0,
    'presence_penalty':0.6}    
}

# Função para serializar o dicionário em JSON e salvar em disco
def save_settings(settings, arquivo):
    with open(arquivo, 'w') as f:
        json.dump(settings, f)

# Função para ler o JSON do disco e converter em um dicionário
def load_settings(arquivo):
    with open(arquivo, 'r') as f:
        settings = json.load(f)
    return settings

# Uso das funções
arquivo_json = "dados.json"

save_settings(dados, arquivo_json)

Settings = load_settings(arquivo_json)

print(Settings)
