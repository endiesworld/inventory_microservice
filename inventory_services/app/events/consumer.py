import logging
import asyncio
from fastapi import Depends
from app.models.domains.products import redis
from app.apis.products import fn_get_product_by_id
from app.db.repositories import ProductsRepository
from app.db.base import BaseRepository

STREAM_KEY = 'completed_order'
CONSUMER_GROUP_NAME = 'inventory-group'
FROM_ID = '>'
CONSUMER_NAME = 'productt_payment_consumer_1'


def get_repository(repo_type: BaseRepository) :
    from app.models.domains.products import redis
    def get_repo(db: redis = redis):
        return repo_type(db)

    return get_repo

product_repo = get_repository(ProductsRepository)()

async def process_redis_stream():
    
    # Create the consumer group (and stream) if needed...
    try: 
        await redis.xgroup_create(STREAM_KEY, CONSUMER_GROUP_NAME, mkstream=True)
        print('Created consumer group.')
    except Exception as e:
        print('Consumer group already exists, skipped creation.', str(e))
    
    while True:
        try:
            print("Trying to fetch from redis stream....")
            reply = redis.xreadgroup(CONSUMER_GROUP_NAME, CONSUMER_NAME, {STREAM_KEY: FROM_ID}, None)
            print(reply)
        except Exception as e:
            print(str(e))
        # Process the messages
        for _, messages in reply:
            for message in messages:
                mess = message[1]
                product_id = mess['product_id']
                redis.xack(STREAM_KEY, CONSUMER_GROUP_NAME, message[0])
                result = await fn_get_product_by_id(product_id, product_repo)
                print("Inevtory Record: ", result)
        await asyncio.sleep(1)
        