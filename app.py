from flask import Flask, request, jsonify
import pickle

# Inicializar o Flask
app = Flask(__name__)

# Carregar o modelo treinado
with open('modelo.pkl', 'rb') as f:
    modelo = pickle.load(f)

# Rota principal para a previsão
@app.route('/predict', methods=['POST'])
def predict():
    dados = request.get_json()  # Receber dados em JSON
    descricao = dados['descricao']  # Extrair a descrição do JSON
    
    # Fazer a previsão
    predicaoNum = modelo.predict([descricao])[0]
    predicaoNum = int(predicaoNum)
    predicao = str
    match predicaoNum:
        case 0:
            predicao = 'Alinhamento'
        case 1:
            predicao = 'Ar Condicionado'
        case 2:
            predicao = 'Arrefecimento'
        case 3:
            predicao = 'Balanceamento'
        case 4:
            predicao = 'Correias'
        case 5:
            predicao = 'Discos e Pastilhas'
        case 6:
            predicao = 'Embreagens'
        case 7:
            predicao = 'Filtros'
        case 8:
            predicao = 'Velas de Ignição'
        case _:
            predicao = 'Nenhum problema'

    # Retornar o resultado como JSON
    return jsonify({'predicao': predicao})

# Página inicial para interface web (opcional)
@app.route('/')
def index():
    return "API de Previsão de Diagnósticos"

if __name__ == '__main__':
    app.run(debug=True)