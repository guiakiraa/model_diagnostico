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
    predicao = modelo.predict([descricao])[0]
    
    # Retornar o resultado como JSON
    return jsonify({'predicao': int(predicao)})

# Página inicial para interface web (opcional)
@app.route('/')
def index():
    return "API de Previsão de Diagnósticos"

if __name__ == '__main__':
    app.run(debug=True)