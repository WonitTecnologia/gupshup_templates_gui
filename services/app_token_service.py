# services/app_token_service.py
# serviço para buscar o token de serviço, para utilizar em apps.
import requests
import time
from models.app_token import AppToken
from config.api_config import URL_PARTNER

class AppTokenService:
    def __init__(self, app_id, partner_service):
        self.app_id = app_id
        self.partner_service = partner_service  # Instância de PartnerService para autenticação
        self.app_token = AppToken()  # Instância de AppToken para armazenar o token do app

    def fetch_app_token(self):
        """Faz uma requisição para obter o TOKEN_APP e armazená-lo."""
        url = f"{URL_PARTNER}partner/app/{self.app_id}/token"
        headers = self.partner_service.get_headers()  # Obtem headers com token de autenticação

        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            # Extrai o token do dicionário JSON aninhado
            token_app = response.json().get('token', {}).get('token')
            if token_app:
                self.app_token.set_token_app(token_app)  # Armazena o TOKEN_APP no modelo
                print("TOKEN_APP obtido e armazenado com sucesso.")
            else:
                print("Não foi possível obter o TOKEN_APP.")
        else:
            print(f"Erro ao obter TOKEN_APP: {response.status_code} - {response.text}")
            raise Exception("Não foi possível obter o TOKEN_APP.")

    def get_app_token(self):
        """Retorna o TOKEN_APP armazenado no modelo AppToken."""
        return self.app_token.get_token_app()

    def refresh_app_token(self):
        """Atualiza o token do app chamando o método fetch_app_token, aguardando 60 segundos."""
        try:
            print("Renovando o TOKEN_APP... Aguardando 60 segundos...")
            time.sleep(60)  # Aguarda 60 segundos
            self.fetch_app_token()
            print("TOKEN_APP renovado com sucesso.")
        except Exception as e:
            print(f"Erro ao renovar o TOKEN_APP: {e}")
            raise Exception("Não foi possível renovar o TOKEN_APP.")
