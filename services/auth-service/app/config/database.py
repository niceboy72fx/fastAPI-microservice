import aioredis
from aioredis import Redis

class RedisManager:
    def __init__(self, redis_url: str, minsize: int = 1, maxsize: int = 10, database_number: int):
        self.redis_url = redis_url
        self.minsize = minsize
        self.maxsize = maxsize
        self.database_number = database_number
        self.redis: Redis | None = None

    async def connect(self):
        if not self.redis:
            self.redis = await aioredis.from_url(
                self.redis_url,
                encoding="utf-8",
                decode_responses=True,
            )
        print("Redis connection established.")

    async def disconnect(self):
        if self.redis:
            await self.redis.close()
            self.redis = None
            print("Redis connection closed.")

    async def set(self, key: str, value: str, expire: int = None):
        if self.redis:
            await self.redis.set(key, value, ex=expire)

    async def get(self, key: str):
        if self.redis:
            return await self.redis.get(key)

    async def delete(self, key: str):
        if self.redis:
            await self.redis.delete(key)

    async def publish(self, channel: str, message: str):
        if self.redis:
            await self.redis.publish(channel, message)
        if self.redis:
            pubsub = self.redis.pubsub()
            await pubsub.subscribe(channel)
            return pubsub

class DatabaseManager:
    def __init__(self, database_url: str, database_username: str, database_password: str):
        self.database_url = database_url
        self.database_username = database_username
        self.database_password = database_password
