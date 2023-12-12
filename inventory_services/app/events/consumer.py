import asyncio

from app.models.domains.products import redis

STREAM_KEY = 'completed_order'
CONSUMER_GROUP_NAME = 'inventory-group'
FROM_ID = '>'
CONSUMER_NAME = 'productt_payment_consumer_1'

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
                print("Unprocessed message: ", message)
                mess = message[1]
                print(f"processed Message: {mess}")
                redis.xack(STREAM_KEY, CONSUMER_GROUP_NAME, message[0])
        await asyncio.sleep(1)
        