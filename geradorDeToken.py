import requests
# Substitua pelos seus valores
tenant_id = "SEU_TENANT_ID_AQUI"
client_id = "SEU_CLIENT_ID_AQUI"
client_secret = "SUA_CLIENT_SECRET_AQUI"

# URL para obter o token
token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

# Dados para a requisição
data = {
    "client_id": client_id,
    "client_secret": client_secret,
    "scope": "https://graph.microsoft.com/.default",
    "grant_type": "client_credentials"
}

# Faz a requisição para obter o token
response = requests.post(token_url, data=data)

if response.status_code == 200:
    token_info = response.json()
    access_token = token_info.get("access_token")
    print("Token gerado com sucesso!")
    print(access_token)
else:
    print("Erro ao gerar token:", response.status_code, response.text)
