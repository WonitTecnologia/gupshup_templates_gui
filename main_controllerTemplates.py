# main_test.py

from controllers.apps_controller import AppsController
from controllers.template_controller import TemplateController

def main(email,password):
    # Dados de login
    email = email
    password = password

    # Cria uma instância do AppsController com as credenciais
    apps_controller = AppsController(email, password)

    # Lista todos os apps disponíveis
    apps_controller.list_apps()  # Chama o método para listar os apps

    # Pede ao usuário para selecionar um app pelo ID
    app_ids = [app.get_app_id() for app in apps_controller.apps_service.Apps]  # Obtém todos os IDs dos apps

    app_id_choice = input("Digite o ID do aplicativo desejado: ")

    if app_id_choice in app_ids:
        # Cria uma instância do TemplateController com o app_id selecionado
        template_controller = TemplateController(email, password) 
        # Obtém e apresenta os templates
        template_controller.get_templates(app_id_choice)
    else:
        print("ID de aplicativo inválido. Por favor, verifique e tente novamente.")

if __name__ == "__main__":
    email = input("Digite seu e-mail: ")
    password = input("Digite sua senha: ")
    main(email,password)
