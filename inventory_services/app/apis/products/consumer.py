from fastapi import BackgroundTasks
import asyncio
import time

from app.models.domains.products import NewProduct, Product, redis

KEY = 'completed_order'
GROUP = 'inventory-group'

async def process_redis_stream():
    redis.delete(KEY)
    redis.xgroup_create(KEY, GROUP, mkstream=True)

    timeout = 100
    retries = 0
    recovery = True
    from_id = '0'
    name = 'productt_payment_consumer_1'
    while True:
        try:
            print("Trying to fetch from redis stream....")
            reply = redis.xreadgroup(GROUP, KEY, {KEY: '>'}, None)
            print(reply)
        except Exception as e:
            print(str(e))
        await asyncio.sleep(1)
            
        # count = 1 
        # reply = redis.xreadgroup(GROUP, name, {KEY: from_id}, count=count, block=timeout)
        # if not reply:
        #     if retries == 5:
        #         print(f'{name}: Waited long enough - bye bye...')
        #         break
        #     retries += 1
        #     timeout *= 2
        #     continue

        # timeout = 100
        # retries = 0

        # if recovery:
        #     # Verify that there are messages to recover. The zeroth member of the
        #     # reply contains the following:
        #     #
        #     # At element 0: the name of the stream
        #     #
        #     # At element 1: a list of pending messages, if any.
        #     #
        #     # If there are messages, we recover them.
        #     #
        #     # Example contents for "reply":
        #     #
        #     # [['numbers', [('1557775037438-0', {'n': '8'})]]]
        #     if reply[0][1]:
        #         print(f'{name}: Recovering pending messages...')
        #     else:
        #         # If there are no messages to recover, switch to fetching new messages
        #         # and call xreadgroup again.
        #         recovery = False
        #         from_id = '>'
        #         continue

        # # Process the messages
        # for _, messages in reply:
        #     for message in messages:
        #         print("Unprocessed message: ", message)
        #         mess = message[1]['n']
        #         print(f"processed Message: {mess}")
        #         redis.xack(KEY, GROUP, message[0])
                
# async def startup_event():
#     # You can add this function to run the background task on startup
#     asyncio.create_task(process_redis_stream())