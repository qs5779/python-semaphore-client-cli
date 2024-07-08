from _typeshed import Incomplete
from semaphore_client.configuration import Configuration as Configuration

class Event:
    swagger_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, project_id: Incomplete | None = None, user_id: Incomplete | None = None, description: Incomplete | None = None, _configuration: Incomplete | None = None) -> None: ...
    @property
    def project_id(self): ...
    @project_id.setter
    def project_id(self, project_id) -> None: ...
    @property
    def user_id(self): ...
    @user_id.setter
    def user_id(self, user_id) -> None: ...
    @property
    def description(self): ...
    @description.setter
    def description(self, description) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
