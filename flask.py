from flask import Flask, request
import requests

app = Flask(__name__)

# Substitua pelo seu token e URL do WhatsApp API
whatsapp_api_url = "https://api.whatsapp.com/send"
whatsapp_token = "seu_token"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data['messages'][0]['text']
    user_id = data['messages'][0]['from']
    
    response = chatbot_response(message)  # Chama a função chatbot_response
    send_message(user_id, response)
    
    return 'OK', 200

def send_message(user_id, message):
    payload = {
        'phone': user_id,
        'body': message,
        'token': whatsapp_token
    }
    requests.post(whatsapp_api_url, data=payload)

def chatbot_response(message):
    if 'olá' in message or 'oi' in message:
        return "Olá! Como posso ajudar você hoje? Escolha uma opção:\n1. Vendedor\n2. Setor de Compras\n3. Entrega e Fretes\n4. Administração"
    else:
        return "Desculpe, não entendi sua mensagem."

if __name__ == '__main__':
    app.run(debug=True)
