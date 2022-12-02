import collections
import dataclasses
import databases
import textwrap
import redis

from pydoc import doc
from quart import Quart, g, request, abort
from quart_schema import QuartSchema, RequestSchemaValidationError, validate_request

app = Quart(__name__)
QuartSchema(app)

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, charset='utf-8', decode_responses=True)

@dataclasses.dataclass
class LeaderboardInformation:
    username: str
    score: int
