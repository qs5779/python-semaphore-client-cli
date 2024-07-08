from _typeshed import Incomplete
from semaphore_client.configuration import Configuration as Configuration

class Environment:
    swagger_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, id: Incomplete | None = None, name: Incomplete | None = None, project_id: Incomplete | None = None, password: Incomplete | None = None, json: Incomplete | None = None, env: Incomplete | None = None, _configuration: Incomplete | None = None) -> None: ...
    @property
    def id(self): ...
    @id.setter
    def id(self, id) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def project_id(self): ...
    @project_id.setter
    def project_id(self, project_id) -> None: ...
    @property
    def password(self): ...
    @password.setter
    def password(self, password) -> None: ...
    @property
    def json(self): ...
    @json.setter
    def json(self, json) -> None: ...
    @property
    def env(self): ...
    @env.setter
    def env(self, env) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
