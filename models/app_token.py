# models/app_token.py

class AppToken:
    def __init__(self):
        self._token_app = None  # Token do app armazenado como privado

    def get_token_app(self):
        """Retorna o token do app armazenado."""
        return self._token_app

    def set_token_app(self, token_app):
        """Define um novo valor para o token do app."""
        self._token_app = token_app
