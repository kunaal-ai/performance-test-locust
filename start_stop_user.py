from locust import User, constant,task

class StartStopUser(User):
    wait_time = constant(1)

    def on_start(self) -> None:
        print("On Start")

    @task
    def task_one(self):
        print("Task one is on run")

    def on_stop(self):
        print("Stopping")