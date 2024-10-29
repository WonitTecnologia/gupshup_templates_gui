# controllers/template_controller.py

from services.partner_service import PartnerService
from services.app_token_service import AppTokenService
from services.template_service import TemplateService

class TemplateController:
    def __init__(self, email, password):
        self.partner_service = PartnerService(email, password)
        self.app_token_service = None  # Inicializado após definir o app_id
        self.template_service = None  # Inicializado após obter o token do app

    def get_templates(self, app_id):
        """
        Obtém e apresenta os templates para um determinado app_id.

        Args:
            app_id (str): O ID da aplicação Gupshup.
        """
        try:
            # 1. Obter token do parceiro (se necessário)
            self.partner_service.get_token()

            # 2. Obter token da aplicação
            self.app_token_service = AppTokenService(app_id, self.partner_service)
            self.app_token_service.fetch_app_token()

            # 3. Obter e apresentar templates
            self.template_service = TemplateService(self.app_token_service)
            self.template_service.fetch_templates(app_id)
            self.template_service.present_templates()

        except Exception as e:
            print(f"Erro ao obter templates: {e}")
