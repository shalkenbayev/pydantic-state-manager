from src.base_redis_state_model import BaseRedisStateModel


class DistributedTaskState(BaseRedisStateModel):
    current_state: str = "scheduled"


task_state = DistributedTaskState(id_="task_1")
task_state.current_state = "running"
task_state.current_state = "completed"
