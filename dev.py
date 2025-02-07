def chatbot_response(message):
    # Mensagem inicial de boas-vindas
    if 'olá' in message or 'oi' in message:
        return "Olá! Como posso ajudar você hoje? Escolha uma opção:\n1. Vendedor\n2. Setor de Compras\n3. Entrega e Fretes\n4. Administração\nDigite o número da opção desejada."

    # Atendimento ao Vendedor
    elif 'vendedor' in message or '1' in message:
        return "Você escolheu o atendimento com o Vendedor. Como posso ajudar em relação aos nossos produtos?"

    # Setor de Compras
    elif 'compras' in message or '2' in message:
        return "Você escolheu o Setor de Compras. Gostaria de mais informações sobre nossos produtos ou fazer um pedido?"

    # Entrega e Fretes
    elif 'entrega' in message or 'frete' in message or '3' in message:
        return "Você escolheu Entrega e Fretes. Qual é o seu endereço ou qual dúvida você tem sobre a entrega?"

    # Administração
    elif 'administração' in message or '4' in message:
        return "Você escolheu a Administração. Como posso ajudar você com questões administrativas?"

    # Caso o usuário digite algo não reconhecido
    else:
        return "Desculpe, não entendi sua mensagem. Por favor, escolha uma opção entre:\n1. Vendedor\n2. Setor de Compras\n3. Entrega e Fretes\n4. Administração"

# Exemplo de interações com o chatbot
print(chatbot_response("olá"))  # Saída: Olá! Como posso ajudar você hoje? Escolha uma opção...
print(chatbot_response("1"))    # Saída: Você escolheu o atendimento com o Vendedor...
print(chatbot_response("2"))    # Saída: Você escolheu o Setor de Compras...
print(chatbot_response("entrega"))  # Saída: Você escolheu Entrega e Fretes...
print(chatbot_response("administração"))  # Saída: Você escolheu a Administração...
print(chatbot_response("qualquer outra mensagem"))  # Saída: Desculpe, não entendi sua mensagem...
