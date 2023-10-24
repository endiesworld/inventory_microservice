from typing import Any, Callable, Type

from redis_om import redis
from fastapi import Depends, Request

from app.db.base import BaseRepository


def get_database(request: Request):
    return request.app.state.db


def get_repository(repo_type: Type[BaseRepository]) -> Callable:
    def get_repo(db: redis = Depends(get_database)) -> Any:
        return repo_type(db)

    return get_repo
