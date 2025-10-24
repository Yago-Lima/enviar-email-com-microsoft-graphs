# Passo a passo para consumir a API de e-mails do Microsoft Graph

## 1. No Entra ID:
- Registrar o app
- Definir para apenas contas no diretório local
- Registrar a secret e salvar para uso posterior
- Dar a permissão **Mail.Send** do tipo **Aplicativo** do Microsoft Graph
- Conceder consentimento de administrador
- Salvar as informações que aparecem em visão geral:
  - **tenant_id** (Id do locatário)
  - **client_id** (Id do aplicativo)

## 2. Utilizar as informações acima para preencher no programa `geradorDeToken.py`

## 3. Com o token gerado pelo `geradorDeToken.py`:
- Editar o código `enviar-email.py` e adicionar o token
- Em `email_data`, mudar o e-mail contido em `address` para o e-mail de destino
- Editar a URL e adicionar o `Object_id` ou e-mail do usuário que está enviando:

```
https://graph.microsoft.com/v1.0/users/{object_id ou email}/sendMail
```

## 4. Executar o código
Se tudo foi configurado corretamente, você deve ter o seguinte output:

```
print("E-mail enviado com sucesso!")
```

## 5. Basta configurar seu e-mail e pronto!
Sua criatividade é o limite.
