# services/template_service.py

import requests
from models.template import Template
from config.api_config import URL_PARTNER

class TemplateService:
    def __init__(self, app_token_service):
        self.app_token_service = app_token_service  # Instância de AppTokenService para autenticação
        self.templates = []  # Lista para armazenar templates

    def fetch_templates(self, app_id):
        """Faz uma requisição para obter templates e os armazena na lista."""
        url = f"{URL_PARTNER}partner/app/{app_id}/templates"
        headers = {
            'Authorization': f'Bearer {self.app_token_service.get_app_token()}',  # Obtém o token da aplicação
            'Content-Type': 'application/json'
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json().get('templates', [])
            for item in data:
                template = Template()
                template.set_app_id(item.get('appId'))
                template.set_button_supported(item.get('buttonSupported'))
                template.set_category(item.get('category'))
                template.set_container_meta(item.get('containerMeta'))
                template.set_created_on(item.get('createdOn'))
                template.set_data(item.get('data'))
                template.set_element_name(item.get('elementName'))
                template.set_external_id(item.get('externalId'))
                template.set_id(item.get('id'))
                template.set_internal_category(item.get('internalCategory'))
                template.set_internal_type(item.get('internalType'))
                template.set_language_code(item.get('languageCode'))
                template.set_language_policy(item.get('languagePolicy'))
                template.set_meta(item.get('meta'))
                template.set_modified_on(item.get('modifiedOn'))
                template.set_namespace(item.get('namespace'))
                template.set_priority(item.get('priority'))
                template.set_quality(item.get('quality'))
                template.set_retry(item.get('retry'))
                template.set_stage(item.get('stage'))
                template.set_status(item.get('status'))
                template.set_template_type(item.get('templateType'))
                template.set_vertical(item.get('vertical'))
                template.set_waba_id(item.get('wabaId'))

                self.templates.append(template)  # Adiciona o template à lista
            print("Templates obtidos com sucesso.")
        else:
            print(f"Erro ao obter templates: {response.status_code} - {response.text}")
            raise Exception("Não foi possível obter os templates.")

    def present_templates(self):
        """Apresenta os templates de maneira formatada."""
        if not self.templates:
            print("Nenhum template disponível.")
            return

        for template in self.templates:
            print(template)  # Chama o método __str__ da classe Template
