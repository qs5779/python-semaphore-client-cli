from _typeshed import Incomplete
from semaphore_client.configuration import Configuration as Configuration

class IntegrationExtractValue:
    swagger_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, id: Incomplete | None = None, name: Incomplete | None = None, value_source: Incomplete | None = None, body_data_type: Incomplete | None = None, key: Incomplete | None = None, variable: Incomplete | None = None, integration_id: Incomplete | None = None, _configuration: Incomplete | None = None) -> None: ...
    @property
    def id(self): ...
    @id.setter
    def id(self, id) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def value_source(self): ...
    @value_source.setter
    def value_source(self, value_source) -> None: ...
    @property
    def body_data_type(self): ...
    @body_data_type.setter
    def body_data_type(self, body_data_type) -> None: ...
    @property
    def key(self): ...
    @key.setter
    def key(self, key) -> None: ...
    @property
    def variable(self): ...
    @variable.setter
    def variable(self, variable) -> None: ...
    @property
    def integration_id(self): ...
    @integration_id.setter
    def integration_id(self, integration_id) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
