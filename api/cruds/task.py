from sqlalchemy.ext.asyncio import AsyncSession

import api.models.task as task_model
import api.schemas.task as task_schema

# async def関数んが非同期処理を行う子ルーチン関数として定義
async def create_task(
  db: AsyncSession, task_create: task_schema.TaskCreate
) -> task_model.Task:
  # 引数のtask_schema.TaskCreateをDBモデルであるtask_model.Taskへ変換する
  task = task_model.Task(**task_create.dict())
  db.add(task)
  # コミットする
  await db.commit()
  # DB上のデータを元にTackインスタンスを更新する（この場合、作成したレコードのidを取得する）
  await db.refresh(task)
  return task