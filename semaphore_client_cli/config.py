"""Top level module config in semaphore_client_cli package."""

from pathlib import Path
from typing import Any, Optional

import click
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from semaphore_client.configuration import Configuration
from wtforglib.files import load_yaml_file
from wtforglib.options import Options


def _load_config_file(config: str, debug: bool) -> dict[str, Any]:
    """Load the configuration file."""
    if not config:
        home = Path.home()
        base = "semaphore-client.yaml"
        config_paths = (
            home / ".config" / base,
            home / ".{0}".format(base),
            Path("/etc/{0}.yaml".format(base)),
        )
        for cp in config_paths:
            if cp.is_file():
                config = str(cp)
                break
    if debug:
        click.echo("DEBUG: config file => {0}".format(config))
    return load_yaml_file(config, missing_ok=False)


class AppConfig:
    """App configuration."""

    opts: Options
    settings: dict[str, str]

    def __init__(self) -> None:
        self.opts = Options()
        self.settings = {}
        self._initialized = False

    def initialize(self, options: Options, ll: str) -> None:
        """Initialize AppConfig.

        Parameters
        ----------
        opts : Options
            Options object
        ll : str
            Log level
        """
        if self._initialized:
            return
        debug = options.options.get("debug", False)
        self.opts = options
        config = Configuration()
        if debug or ll == "DEBUG":
            config.debug = True
        self.settings = _load_config_file(  # noqa: WPS221
            str(options.options.get("config", "")),
            bool(debug),
        )
        for key in ("host", "username", "password"):
            setattr(config, key, self.settings.get(key, ""))
        Configuration.set_default(config)
        self._initialized = True


class LocalConfig(BaseModel):
    """Local configurations."""

    ignore_me: bool = False


class GlobalConfig(BaseSettings):
    """Global configurations."""

    # These variables will be loaded from the .env file. However, if
    # there is a shell environment variable having the same name,
    # that will take precedence.

    local_config: LocalConfig = LocalConfig()

    # define global variables with the Field class
    env_state: Optional[str] = Field(None)
    # environment specific variables do not need the Field class
    log_level: str = "DEBUG"

    model_config = SettingsConfigDict(extra="ignore", env_file=".env")


class DevConfig(GlobalConfig):
    """Development configurations."""


class ProdConfig(GlobalConfig):
    """Production configurations."""


class FactoryConfig:
    """Returns a config instance depending on the ENV_STATE variable."""

    def __init__(self, env_state: Optional[str]):
        """Construct a FactoryConfig instance.

        Parameters
        ----------
        env_state : Optional[str]
            The environment state for the app, defaults to dev
        """
        self.env_state = env_state

    def __call__(self) -> GlobalConfig:
        """Return the appropriate config based on environment."""
        if self.env_state == "prod":
            return ProdConfig(env_prefix="PROD_")  # type: ignore [call-arg]

        return DevConfig(env_prefix="DEV_")  # type: ignore [call-arg]


cfg = FactoryConfig(GlobalConfig().env_state)()  # type: ignore [call-arg]

app_cfg = AppConfig()
