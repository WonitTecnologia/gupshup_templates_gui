import requests
from models.partner_app import PartnerApp
from config.api_config import URL_PARTNER

class AppsService:
    def __init__(self, token):
        self.token = token  # Token para autenticação
        self.Apps = []  # Lista para armazenar PartnerApps

    def fetch_apps(self):
        """Faz uma requisição para obter os apps e os armazena na lista."""
        url = f"{URL_PARTNER}partner/account/api/partnerApps"
        headers = {
            'Authorization': f'{self.token}',  # Obtém o token da aplicação
            'Content-Type': 'application/json'
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            # Aqui assumimos que a resposta pode ser um dicionário contendo uma lista de aplicativos
            apps_data = response.json()  # Converte a resposta em JSON
            #print("Resposta da API:", apps_data)  # Adicionado para debug
            
            # Verifique se a resposta contém uma chave com a lista de apps
            if 'partnerAppsList' in apps_data:  # Exemplo, ajuste conforme a estrutura real da resposta
                apps_data = apps_data['partnerAppsList']  # Ajuste para o caminho correto

            # Verifique se apps_data é uma lista
            if isinstance(apps_data, list):
                for app_data in apps_data:
                    if isinstance(app_data, dict):  # Certifique-se de que app_data é um dicionário
                        partner_app = PartnerApp()
                        partner_app.set_app_id(app_data.get("id"))
                        partner_app.set_name(app_data.get("name"))
                        partner_app.set_customer_id(app_data.get("customerId"))
                        partner_app.set_live(app_data.get("live"))
                        partner_app.set_partner_id(app_data.get("partnerId"))
                        partner_app.set_created_on(app_data.get("createdOn"))
                        partner_app.set_modified_on(app_data.get("modifiedOn"))
                        partner_app.set_partner_created(app_data.get("partnerCreated"))
                        partner_app.set_cxp_enabled(app_data.get("cxpEnabled"))
                        partner_app.set_partner_usage(app_data.get("partnerUsage"))
                        partner_app.set_stopped(app_data.get("stopped"))
                        partner_app.set_healthy(app_data.get("healthy"))
                        partner_app.set_cap(app_data.get("cap"))
                        partner_app.set_phone(app_data.get("phone"))

                        self.Apps.append(partner_app)  # Adiciona à lista de Apps
                    else:
                        print("Item não é um dicionário:", app_data)  # Debug para itens não dicionário
            else:
                print("Resposta não é uma lista:", apps_data)  # Debug para resposta não lista
        else:
            print(f"Erro ao obter aplicativos: {response.status_code} - {response.text}")
            raise Exception("Não foi possível obter os aplicativos.")

    def list_app_ids(self):
        """Lista todos os app_ids armazenados na lista Apps."""
        if not self.Apps:
            print("Nenhum aplicativo disponível.")
            return

        print("Lista de App IDs:")
        for app in self.Apps:
            print(app.get_app_id())  # Chama o getter para obter o app_id

# Exemplo de uso:
# apps_service = AppsService(token="seu_token_aqui")
# apps_service.fetch_apps()
# apps_service.list_app_ids()
