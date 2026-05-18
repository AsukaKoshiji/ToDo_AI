from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


class TodoBase(BaseModel):
    title: str = Field(
        ...,
        json_schema_extra={"example": "買い物に行く"}
    )
    description: Optional[str] = Field(
        "",
        json_schema_extra={"example": "牛乳を買う"}
    )
    completed: bool = Field(
        False,
        json_schema_extra={"example": False}
    )


class TodoResponse(TodoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)