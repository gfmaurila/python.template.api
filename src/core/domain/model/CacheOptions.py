from dataclasses import dataclass

@dataclass
class CacheOptions:
    AbsoluteExpirationInHours: int
    SlidingExpirationInSeconds: int
    DbIndex: int = 0
