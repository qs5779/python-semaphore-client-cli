from _typeshed import Incomplete
from semaphore_client.configuration import Configuration as Configuration

class RepositoryRequest:
    swagger_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, name: Incomplete | None = None, project_id: Incomplete | None = None, git_url: Incomplete | None = None, git_branch: Incomplete | None = None, ssh_key_id: Incomplete | None = None, _configuration: Incomplete | None = None) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def project_id(self): ...
    @project_id.setter
    def project_id(self, project_id) -> None: ...
    @property
    def git_url(self): ...
    @git_url.setter
    def git_url(self, git_url) -> None: ...
    @property
    def git_branch(self): ...
    @git_branch.setter
    def git_branch(self, git_branch) -> None: ...
    @property
    def ssh_key_id(self): ...
    @ssh_key_id.setter
    def ssh_key_id(self, ssh_key_id) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
