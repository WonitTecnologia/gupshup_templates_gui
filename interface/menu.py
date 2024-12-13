class Menu:
    def __init__(self, template_controller, app_id):
        self.template_controller = template_controller
        self.app_id = app_id

    def show(self):
        while True:
            print("\n--- Menu ---")
            print("1 - Visualizar todos os templates")
            print("2 - Criar template (Básico)")
            print("3 - Criar templates por CSV")
            print("4 - Backup de templates")
            print("5 - Remover templates por CSV")
            print("6 - Remover template por ID")
            print("0 - Sair")

            choice = input("Escolha uma opção: ")

            if choice == "1":
                self.view_templates()
            elif choice == "2":
                self.create_template()
            elif choice == "3":
                self.create_templates_from_csv()
            elif choice == "4":
                self.backup_templates()
            elif choice == "5":
                self.remove_templates_from_csv()
            elif choice == "6":
                self.remove_template_by_id()
            elif choice == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def view_templates(self):
        print("Visualizando todos os templates...")
        self.template_controller.get_templates(self.app_id)

    def create_template(self):
        """
        Coleta as informações do usuário, incluindo exemplos para as variáveis, 
        e cria um template.
        """
        print("Criando template...")

        while True:
            name = input("Digite o nome do modelo (apenas letras minúsculas, sem espaços e"
                        " sem caracteres especiais, exceto '_'): ")
            if name.islower() and all(c.isalnum() or c == '_' for c in name):
                break
            else:
                print("Nome inválido. Tente novamente.")

        while True:
            try:
                num_variables = int(input("Quantas variáveis o template terá? "))
                if num_variables >= 0:
                    break
                else:
                    print("Número inválido. Digite um número não negativo.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

        if num_variables == 0:
            content = input("Digite o conteúdo do template (sem variáveis): ")
            example = content  # Se não tem variáveis, o exemplo é o próprio conteúdo
        else:
            print("Digite o texto, marcando as posições das variáveis com '$1', '$2', etc.:")
            content = input()
            for i in range(1, num_variables + 1):
                while f"${i}" not in content:
                    print(f"Variável ${i} não encontrada no texto. Digite o texto novamente:")
                    content = input()

            # Coleta os exemplos para as variáveis
            example_values = []
            for i in range(1, num_variables + 1):
                example_value = input(f"Digite o exemplo para a variável ${i}: ")
                example_values.append(example_value)

            # Substitui '$1', '$2', etc. pelos exemplos no conteúdo
            example = content
            for i, value in enumerate(example_values):
                example = example.replace(f"${i+1}", value)

            # Substitui '$1', '$2', etc. por '{{1}}', '{{2}}', etc. no conteúdo para o envio
            content_to_send = content
            for i in range(1, num_variables + 1):
                content_to_send = content_to_send.replace(f"${i}", f"{{{{{i}}}}}")  # Correção para usar '{{1}}' etc.

            print("Content send: ")
            print(content_to_send)
            print("Content example: ")
            print(example)

        # Define a categoria como 'UTILITY' e o idioma como 'pt_BR'
        category = "UTILITY"
        language_code = "pt_BR"

        self.template_controller.create_template(
            self.app_id, name, category, language_code, content_to_send, example
        )

    def create_templates_from_csv(self):
        print("Criando templates a partir de um arquivo CSV...")
        csv_path = input("Digite o caminho do arquivo CSV: ")
        self.template_controller.create_templates_from_csv(self.app_id, csv_path)

    def backup_templates(self):
        print("Realizando backup dos templates...")
        self.template_controller.backup_templates(self.app_id)

    def remove_templates_from_csv(self):
        print("Removendo templates a partir de um arquivo CSV...")
        csv_path = input("Digite o caminho do arquivo CSV: ")
        self.template_controller.remove_templates_from_csv(self.app_id, csv_path)

    def remove_template_by_id(self):
        print("Removendo template por ID...")
        template_id = input("Digite o ID do template: ")
        self.template_controller.remove_template_by_id(self.app_id, template_id)
