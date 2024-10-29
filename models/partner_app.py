# models/partner_app.py

class PartnerApp:
    def __init__(self):
        self._app_id = None
        self._name = None
        self._customer_id = None
        self._live = None
        self._partner_id = None
        self._created_on = None
        self._modified_on = None
        self._partner_created = None
        self._cxp_enabled = None
        self._partner_usage = None
        self._stopped = None
        self._healthy = None
        self._cap = None
        self._phone = None

    # Getters
    def get_app_id(self):
        """Retorna o ID da aplicação."""
        return self._app_id

    def get_name(self):
        """Retorna o nome da aplicação."""
        return self._name

    def get_customer_id(self):
        """Retorna o ID do cliente."""
        return self._customer_id

    def get_live(self):
        """Retorna o status ao vivo da aplicação."""
        return self._live

    def get_partner_id(self):
        """Retorna o ID do parceiro."""
        return self._partner_id

    def get_created_on(self):
        """Retorna a data de criação."""
        return self._created_on

    def get_modified_on(self):
        """Retorna a data de modificação."""
        return self._modified_on

    def get_partner_created(self):
        """Retorna se o parceiro foi criado."""
        return self._partner_created

    def get_cxp_enabled(self):
        """Retorna se o CXP está habilitado."""
        return self._cxp_enabled

    def get_partner_usage(self):
        """Retorna se o uso do parceiro está habilitado."""
        return self._partner_usage

    def get_stopped(self):
        """Retorna se a aplicação está parada."""
        return self._stopped

    def get_healthy(self):
        """Retorna o status de saúde da aplicação."""
        return self._healthy

    def get_cap(self):
        """Retorna a capacidade da aplicação."""
        return self._cap

    def get_phone(self):
        """Retorna o telefone da aplicação."""
        return self._phone

    # Setters
    def set_app_id(self, app_id):
        """Define o ID da aplicação."""
        self._app_id = app_id

    def set_name(self, name):
        """Define o nome da aplicação."""
        self._name = name

    def set_customer_id(self, customer_id):
        """Define o ID do cliente."""
        self._customer_id = customer_id

    def set_live(self, live):
        """Define o status ao vivo da aplicação."""
        self._live = live

    def set_partner_id(self, partner_id):
        """Define o ID do parceiro."""
        self._partner_id = partner_id

    def set_created_on(self, created_on):
        """Define a data de criação."""
        self._created_on = created_on

    def set_modified_on(self, modified_on):
        """Define a data de modificação."""
        self._modified_on = modified_on

    def set_partner_created(self, partner_created):
        """Define se o parceiro foi criado."""
        self._partner_created = partner_created

    def set_cxp_enabled(self, cxp_enabled):
        """Define se o CXP está habilitado."""
        self._cxp_enabled = cxp_enabled

    def set_partner_usage(self, partner_usage):
        """Define se o uso do parceiro está habilitado."""
        self._partner_usage = partner_usage

    def set_stopped(self, stopped):
        """Define se a aplicação está parada."""
        self._stopped = stopped

    def set_healthy(self, healthy):
        """Define o status de saúde da aplicação."""
        self._healthy = healthy

    def set_cap(self, cap):
        """Define a capacidade da aplicação."""
        self._cap = cap

    def set_phone(self, phone):
        """Define o telefone da aplicação."""
        self._phone = phone

    def __str__(self):
        """Retorna uma representação em string do objeto PartnerApp."""
        return (f"PartnerApp(id={self._app_id}, name={self._name}, customerId={self._customer_id}, "
                f"live={self._live}, partnerId={self._partner_id}, createdOn={self._created_on}, "
                f"modifiedOn={self._modified_on}, partnerCreated={self._partner_created}, "
                f"cxpEnabled={self._cxp_enabled}, partnerUsage={self._partner_usage}, "
                f"stopped={self._stopped}, healthy={self._healthy}, cap={self._cap}, "
                f"phone={self._phone})")
