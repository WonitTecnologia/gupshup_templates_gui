# models/template.py

class Template:
    def __init__(self):
        self._app_id = None
        self._button_supported = None
        self._category = None
        self._container_meta = None
        self._created_on = None
        self._data = None
        self._element_name = None
        self._external_id = None
        self._id = None
        self._internal_category = None
        self._internal_type = None
        self._language_code = None
        self._language_policy = None
        self._meta = None
        self._modified_on = None
        self._namespace = None
        self._priority = None
        self._quality = None
        self._retry = None
        self._stage = None
        self._status = None
        self._template_type = None
        self._vertical = None
        self._waba_id = None

    # Getters and Setters
    def get_app_id(self):
        return self._app_id

    def set_app_id(self, app_id):
        self._app_id = app_id

    def get_button_supported(self):
        return self._button_supported

    def set_button_supported(self, button_supported):
        self._button_supported = button_supported

    def get_category(self):
        return self._category

    def set_category(self, category):
        self._category = category

    def get_container_meta(self):
        return self._container_meta

    def set_container_meta(self, container_meta):
        self._container_meta = container_meta

    def get_created_on(self):
        return self._created_on

    def set_created_on(self, created_on):
        self._created_on = created_on

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    def get_element_name(self):
        return self._element_name

    def set_element_name(self, element_name):
        self._element_name = element_name

    def get_external_id(self):
        return self._external_id

    def set_external_id(self, external_id):
        self._external_id = external_id

    def get_id(self):
        return self._id

    def set_id(self, id_):
        self._id = id_

    def get_internal_category(self):
        return self._internal_category

    def set_internal_category(self, internal_category):
        self._internal_category = internal_category

    def get_internal_type(self):
        return self._internal_type

    def set_internal_type(self, internal_type):
        self._internal_type = internal_type

    def get_language_code(self):
        return self._language_code

    def set_language_code(self, language_code):
        self._language_code = language_code

    def get_language_policy(self):
        return self._language_policy

    def set_language_policy(self, language_policy):
        self._language_policy = language_policy

    def get_meta(self):
        return self._meta

    def set_meta(self, meta):
        self._meta = meta

    def get_modified_on(self):
        return self._modified_on

    def set_modified_on(self, modified_on):
        self._modified_on = modified_on

    def get_namespace(self):
        return self._namespace

    def set_namespace(self, namespace):
        self._namespace = namespace

    def get_priority(self):
        return self._priority

    def set_priority(self, priority):
        self._priority = priority

    def get_quality(self):
        return self._quality

    def set_quality(self, quality):
        self._quality = quality

    def get_retry(self):
        return self._retry

    def set_retry(self, retry):
        self._retry = retry

    def get_stage(self):
        return self._stage

    def set_stage(self, stage):
        self._stage = stage

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    def get_template_type(self):
        return self._template_type

    def set_template_type(self, template_type):
        self._template_type = template_type

    def get_vertical(self):
        return self._vertical

    def set_vertical(self, vertical):
        self._vertical = vertical

    def get_waba_id(self):
        return self._waba_id

    def set_waba_id(self, waba_id):
        self._waba_id = waba_id

    def __str__(self):
        return f"Template(ID: {self.get_id()}, Name: {self.get_element_name()}, Texto: {self.get_data()}, Category: {self.get_category()}, Status: {self.get_status()})"
