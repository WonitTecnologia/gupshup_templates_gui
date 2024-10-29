# models/partner.py

class Partner:
    def __init__(self):
        self._token = None  # Define o token como privado

    def get_token(self):
        """Retorna o token armazenado."""
        return self._token

    def set_token(self, token):
        """Define um novo valor para o token."""
        self._token = token
