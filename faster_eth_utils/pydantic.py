from typing import (
    Any,
)

from pydantic import (
    BaseModel,
)


class CamelModel(BaseModel):
    def model_dump(self, *args: Any, **kwargs: Any) -> dict[str, Any]:
        if "by_alias" in kwargs:
            return super().model_dump(*args, **kwargs)
        return super().model_dump(*args, **kwargs, by_alias=True)


class AnyModel(BaseModel):
    class Config:
        arbitrary_types_allowed = True
