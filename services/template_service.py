# services/template_service.py

import requests
import json
import csv  # Importe o módulo csv
from models.template import Template
from config.api_config import URL_PARTNER

class TemplateService:
    def __init__(self, app_token_service):
        self.app_token_service = app_token_service  # Instância de AppTokenService para autenticação
        self.templates = []  # Lista para armazenar templates

    def set_id(self, id):
        self.id = id
        return id

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

    def backup_templates(self, app_id):
        """
        Realiza o backup dos templates para um determinado app_id em um arquivo CSV.

        Args:
            app_id (str): O ID da aplicação Gupshup.
        """
        try:
            # 1. Obter token da aplicação (já feito no construtor)
            
            # 2. Obter templates (chamando o fetch_templates)
            self.fetch_templates(app_id)

            # 3. Salvar templates em um arquivo CSV
            with open('templates_backup.csv', 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["ID", "Name", "Texto", "Category", "Status"])  # Cabeçalho
                for template in self.templates:  # Usa a lista de templates existente
                    writer.writerow([template.get_id(), template.get_element_name(), template.get_data(), template.get_category(), template.get_status()])

            print("Backup de templates realizado com sucesso em 'templates_backup.csv'")

        except Exception as e:
            print(f"[TemplateService] Erro ao realizar backup dos templates: {e}")

    def create_template(self, app_id, name, category, language_code, content, example):
        """
        Cria um template sem botões na plataforma Gupshup.
            app_id (str): O ID da aplicação Gupshup.
            name (str): O nome do template.
            category (str): A categoria do template.
            language_code (str): O código do idioma do template.
            content (str): O conteúdo do template.
            example (str): O exemplo do template.
        """
        try:
            url = f"{URL_PARTNER}partner/app/{app_id}/templates"
            headers = {
                'Authorization': f'Bearer {self.app_token_service.get_app_token()}',
                'Content-Type': 'application/x-www-form-urlencoded'
            }

            data = {
                'elementName': name,
                'languageCode': language_code,
                'category': category,
                'templateType': "TEXT",
                'vertical': name,
                'content': content,
                'example': example,
                'enableSample': True,
                'allowTemplateCategoryChange': True,
                'buttons': []
            }

            for attempt in range(2):  # Tenta no máximo 2 vezes (incluindo refresh de token)
                response = requests.post(url, headers=headers, data=data)
                
                if response.status_code == 429:  # Limite de requisições
                    print("Limite de requisições atingido. Tentando renovar o token...")
                    self.app_token_service.refresh_app_token()
                    headers['Authorization'] = f'Bearer {self.app_token_service.get_app_token()}'  # Atualiza os headers
                    continue  # Tenta novamente com o novo token

                if response.status_code == 401:  # Token expirado ou inválido
                    print("Token inválido ou expirado. Renovando token...")
                    self.app_token_service.refresh_app_token()
                    headers['Authorization'] = f'Bearer {self.app_token_service.get_app_token()}'
                    continue  # Tenta novamente com o novo token

                if response.status_code in (200, 204):  # Sucesso
                    print("Template criado com sucesso.")
                    return response.json() if response.status_code == 200 else None
                
                elif response.status_code == 400 and "Template Already exists" in response.text:
                    # Tratamento para templates duplicados
                    print("Template já existe, abortando criação.")
                    return {"status": "error", "message": "Template já existe."}

                else:
                    # Outros erros
                    print(f"Erro ao criar template: {response.status_code} - {response.text}")
                    raise Exception("Não foi possível criar o template.")

            # Caso todas as tentativas falhem
            raise Exception(f"Erro após múltiplas tentativas: {response.status_code} - {response.text}")

        except Exception as e:
            print(f"[TemplateService] Erro ao criar template: {e}")
            raise

    def remove_template_by_id(self, app_id, template_id):
            """
            Remove um template baseado no templateid

            Args:
                app_id (str): O ID da aplicação Gupshup.
                template_id (str): O ID do template a ser removido.
            """
            try:
                # 1. Obter os templates
                self.fetch_templates(app_id)

                # 2. Filtrar o template pelo ID
                template_to_remove = None
                for template in self.templates:
                    if template.get_id() == template_id:
                        template_to_remove = template
                        break

                if not template_to_remove:
                    print(f"Template com ID {template_id} não encontrado.")
                    return

                # 3. Obter o nome do template
                element_name = template_to_remove.get_element_name()

                # 4. Construir a URL com o nome e o ID do template
                url = f"{URL_PARTNER}partner/app/{app_id}/template/{element_name}/{template_id}"
                headers = {
                    'Authorization': f'Bearer {self.app_token_service.get_app_token()}',
                }

                # 5. Fazer a requisição DELETE
                response = requests.delete(url, headers=headers)

                if response.status_code == 200:
                    print(f"Template com ID {template_id} removido com sucesso.")
                else:
                    print(f"Erro ao remover template: {response.status_code} - {response.text}")
                    raise Exception("Não foi possível remover o template.")

            except Exception as e:
                print(f"[TemplateService] Erro ao remover template: {e}")