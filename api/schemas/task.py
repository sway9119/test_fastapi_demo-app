from typing import Optional
from pydantic import BaseModel, Field

class TaskBase(BaseModel):
  title: Optional[str] = Field(None, example="クリーニングを取りに行く")


class TaskCreate(TaskBase):
  pass

class TaskCreateResponse(TaskCreate):
  id: int

  class Config:
    # レスポンススキーマTaskCreateResponseが、暗黙的にORMを受け取り、レスポンススキーマに変換する
    orm_mode = True

class Task(TaskBase):
  id: int
  title: Optional[str] = Field(None, example="クローニングを取りに行く")
  done: bool = Field(False, description="完了フラグ")

  class Config:
    orm_mode = True


