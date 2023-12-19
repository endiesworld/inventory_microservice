import asyncio
from app.models.domains.order import redis

from app.db.repositories import OrdersRepository
from app.db.base import BaseRepository

from app.apis.orders import fn_get_order_by_id

STREAM_KEY = 'refund_order'
CONSUMER_GROUP_NAME = 'payment-group'
FROM_ID = '>'
CONSUMER_NAME = 'payment_refund_consumer_1'


def get_repository(repo_type: BaseRepository) :
    def get_repo(db: redis = redis):
        return repo_type(db)

    return get_repo

order_repo = get_repository(OrdersRepository)()

async def process_redis_stream():
    
    # Create the consumer group (and stream) if needed...
    try: 
        await redis.xgroup_create(STREAM_KEY, CONSUMER_GROUP_NAME, mkstream=True)
        print('Created payment refund group.')
    except Exception as e:
        print('Consumer group already exists, skipped creation.', str(e))
    
    while True:
        try:
            print("Trying to fetch failed order from redis stream....")
            reply = redis.xreadgroup(CONSUMER_GROUP_NAME, CONSUMER_NAME, {STREAM_KEY: FROM_ID}, None)
            print(reply)
        except Exception as e:
            print(str(e))
        # Process the messages
        for _, messages in reply:
            for message in messages:
                mess = message[1]
                order_id = mess['pk']
                # Update the redis stream after reading the message
                redis.xack(STREAM_KEY, CONSUMER_GROUP_NAME, message[0])
                # Fetch product from inventory db using product id
                _, order = await fn_get_order_by_id(order_id, order_repo)
                order.status = 'refunded'
                order.save()
        await asyncio.sleep(1)
        