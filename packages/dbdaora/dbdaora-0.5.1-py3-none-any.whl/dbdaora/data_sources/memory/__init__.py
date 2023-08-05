from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Protocol,
    Sequence,
    Tuple,
    Union,
)

from .. import DataSource


RangeOutput = Union[
    Sequence[Tuple[str, float]],
    Sequence[Tuple[bytes, float]],
    Sequence[Union[bytes, str]],
]


class MemoryDataSource(DataSource):
    key_separator: ClassVar[str] = ':'

    def make_key(self, *key_parts: str) -> str:
        return self.key_separator.join(key_parts)

    async def get(self, key: str) -> Optional[bytes]:
        raise NotImplementedError()  # pragma: no cover

    async def set(self, key: str, data: str) -> None:
        raise NotImplementedError()  # pragma: no cover

    async def delete(self, key: str) -> None:
        raise NotImplementedError()  # pragma: no cover

    async def expire(self, key: str, time: int) -> None:
        raise NotImplementedError()  # pragma: no cover

    async def exists(self, key: str) -> int:
        raise NotImplementedError()  # pragma: no cover

    async def zrevrange(
        self, key: str, withscores: bool = False
    ) -> Optional[RangeOutput]:
        raise NotImplementedError()  # pragma: no cover

    async def zrange(
        self, key: str, withscores: bool = False
    ) -> Optional[RangeOutput]:
        raise NotImplementedError()  # pragma: no cover

    async def zadd(
        self, key: str, score: float, member: str, *pairs: Union[float, str]
    ) -> None:
        raise NotImplementedError()  # pragma: no cover

    async def hmset(
        self,
        key: str,
        field: Union[str, bytes],
        value: Union[str, bytes],
        *pairs: Union[str, bytes],
    ) -> None:
        raise NotImplementedError()  # pragma: no cover

    async def hmget(
        self, key: str, field: Union[str, bytes], *fields: Union[str, bytes]
    ) -> Sequence[Optional[bytes]]:
        raise NotImplementedError()  # pragma: no cover

    async def hgetall(self, key: str) -> Dict[bytes, bytes]:
        raise NotImplementedError()  # pragma: no cover

    def pipeline(self) -> 'Pipeline':
        raise NotImplementedError()  # pragma: no cover

    def close(self) -> None:
        raise NotImplementedError()  # pragma: no cover

    async def wait_closed(self) -> None:
        raise NotImplementedError()  # pragma: no cover


class Pipeline(Protocol):
    async def execute(self, *, return_exceptions: bool = False) -> List[Any]:
        raise NotImplementedError()  # pragma: no cover

    def hmget(
        self, key: str, field: Union[str, bytes], *fields: Union[str, bytes]
    ) -> None:
        raise NotImplementedError()  # pragma: no cover

    def hgetall(self, key: str) -> None:
        raise NotImplementedError()  # pragma: no cover

    def exists(self, key: str) -> None:
        raise NotImplementedError()  # pragma: no cover
