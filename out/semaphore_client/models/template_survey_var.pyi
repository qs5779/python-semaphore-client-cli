from _typeshed import Incomplete
from semaphore_client.configuration import Configuration as Configuration

class TemplateSurveyVar:
    swagger_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, name: Incomplete | None = None, title: Incomplete | None = None, description: Incomplete | None = None, type: Incomplete | None = None, required: Incomplete | None = None, _configuration: Incomplete | None = None) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def title(self): ...
    @title.setter
    def title(self, title) -> None: ...
    @property
    def description(self): ...
    @description.setter
    def description(self, description) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type) -> None: ...
    @property
    def required(self): ...
    @required.setter
    def required(self, required) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
