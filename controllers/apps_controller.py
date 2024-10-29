from services.apps_service import AppsService
from services.partner_service import PartnerService

class AppsController:
    def __init__(self, email, password):
        """
        Inicializa o AppsController com as credenciais do parceiro.

        Args:
            email (str): Email do parceiro.
            password (str): Senha do parceiro.
        """
        self.partner_service = PartnerService(email, password)  # Cria a instância do PartnerService
        self.apps_service = None  # Inicializado após obter o token

        # Obtém o token e inicializa o AppsService
        self.initialize()

    def initialize(self):
        """Método para autenticar e inicializar o AppsService."""
        try:
            self.partner_service.get_token()  # Autentica e obtém o token
            token = self.partner_service.get_token()  # Obtém o token
            self.apps_service = AppsService(token)  # Inicializa o AppsService com o token
        except Exception as e:
            print(f"Erro ao inicializar AppsController: {e}")
            raise  # Propaga a exceção

    def list_apps(self):
        """Lista todos os app IDs e seus nomes."""
        try:
            # Chama o método para buscar os aplicativos
            self.apps_service.fetch_apps()
            apps = self.apps_service.Apps

            # Verifica se há aplicativos disponíveis
            if not apps:
                print("Nenhum aplicativo encontrado.")
                return

            print("Lista de App IDs e Nomes:")
            for app in apps:
                # Exibe o app ID e o nome
                print(f"ID: {app.get_app_id()}, Nome: {app.get_name()}")  # Chama os getters para obter os dados

        except Exception as e:
            print(f"Ocorreu um erro: {str(e)}")

# Exemplo de uso:
# controller = AppsController(email="seu_email", password="sua_senha")
# controller.list_apps()
