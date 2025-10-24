import requests

# Token de acesso obtido via MSAL (OAuth2)
access_token = 'SEU_ACCESS_TOKEN_AQUI'

# Cabeçalhos da requisição
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

# Corpo da mensagem
email_data = {
    "message": {
        "subject": "Teste via Microsoft Graph",
        "body": {
            "contentType": "Text",
            "content": "Olá! Este é um e-mail de teste enviado via Microsoft Graph API."
        },
        "toRecipients": [
            {
                "emailAddress": {
                    "address": "destinatario@dominio.com"
                }
            }
        ]
    },
    "saveToSentItems": "true"
}

# Endpoint da API
url = "https://graph.microsoft.com/v1.0/users/8c84268e-2e71-472e-9761-7bf98fe6be3a/sendMail"
# url = "https://graph.microsoft.com/v1.0/users/{object_id ou email}/sendMail"

# Enviando o e-mail
response = requests.post(url, headers=headers, json=email_data)

# Verificando o resultado
if response.status_code == 202:
    print("E-mail enviado com sucesso!")
else:
    print(f"Erro ao enviar e-mail: {response.status_code}")
    print(response.text)