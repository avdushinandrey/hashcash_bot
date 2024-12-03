from pydantic.v1 import BaseModel,
from enum import Enum

class HashEror(str, Enum):
    BLOCK_TIMESTAMP_TOO_LOW = 'BLOCK_TIMESTAMP_TOO_LOW'
    BLOCK_TIMESTAMP_TOO_BIG = 'BLOCK_TIMESTAMP_TOO_BIG'
    INVALID_BLOCK = 'INVALID_BLOCK'
    USER_PROBABLY_BOT_OR_FRAUD = 'USER_PROBABLY_BOT_OR_FRAUD'
    ENERGY_TOO_LOW = 'ENERGY_TOO_LOW'

class HashcashTypes(str,Enum):
    get = 'hashcash.get'
    userStuff = 'user.userStuff'
    submit = 'hashcash.submit'
    userBlock = 'user.userBlock'
    error = 'hashcash.error'
