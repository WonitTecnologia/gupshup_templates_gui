my_project/
│
├── config/
│ └── api_config.py # Configurações de URLs base, tokens, etc.
│
├── services/
│ ├── user_service.py # Classe para chamadas de API do usuário
│ └── product_service.py # Classe para chamadas de API do produto
│
├── models/
│ ├── user.py # Modelo de dados para usuários
│ └── product.py # Modelo de dados para produtos
│
├── controllers/
│ ├── user_controller.py # Lógica para gerenciar usuários
│ └── product_controller.py # Lógica para gerenciar produtos
│
├── utils/
│ ├── json_parser.py # Utilitário para parse de JSON
│ └── error_handler.py # Tratamento de erros
│
└── interfaces/
└── api_interface.py # Interface para padronizar chamadas de API
