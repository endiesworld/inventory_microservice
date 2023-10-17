import os
from distutils.util import strtobool
from typing import List, Optional

from pydantic_settings import BaseSettings

INIT_API_VERSION = "0.0.1"
INIT_API_ALGORITHM = "HS256"
INIT_API_ACCESS_TOKEN_EXPIRY = 3600
INIT_APPLICATION_ID = "inventory_services"
INIT_APPLICATION_NAMESPACE = "inventory_services"


class GlobalConfig(BaseSettings):
    """Global configurations."""

    ENV_STATE: Optional[str] = os.environ.get("ENV_STATE", "dev")
    SECRET_KEY: Optional[str] = os.environ.get("SECRET_KEY", None)
    
    REDIS_PORT: Optional[str] = os.environ.get("REDIS_PORT", None)
    REDIS_CONTAINER_NAME: Optional[str] = os.environ.get("REDIS_CONTAINER_NAME", None)

    APPLICATION_ID: Optional[str] = os.environ.get("APPLICATION_ID", INIT_APPLICATION_ID)
    APPLICATION_CALLBACK_URL: Optional[str] = os.environ.get(
        "APPLICATION_CALLBACK_URL", ""
    )
    API_VERSION: Optional[str] = os.environ.get("API_VERSION", INIT_API_VERSION)
    API_ALGORITHM: Optional[str] = os.environ.get("API_ALGORITHM", INIT_API_ALGORITHM)
    API_ACCESS_TOKEN_EXPIRY: Optional[int] = os.environ.get(
        "API_ACCESS_TOKEN_EXPIRY", INIT_API_ACCESS_TOKEN_EXPIRY
    )
    APPLICATION_NAMESPACE: Optional[str] = os.environ.get(
        "APPLICATION_NAMESPACE", INIT_APPLICATION_NAMESPACE
    )
    APPLICATION_ROOT: Optional[str] = os.environ.get(
        "APPLICATION_ROOT", "http://localhost:3000"
    )
    APPLICATION_NAME: Optional[str] = os.environ.get(
        "APPLICATION_NAME", "inventory_services"
    )
    APPLICATION_LOGO: Optional[str] = os.environ.get("APPLICATION_LOGO", "")


    

    
app_config = GlobalConfig()
# print(config.__repr__())
