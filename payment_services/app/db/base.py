from redis_om import redis 

class BaseRepository:
    def __init__(self, db: redis) -> None:
        self.db = db
