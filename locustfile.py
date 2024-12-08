from locust import HttpUser, task, constant


class HelloWorldUser(HttpUser):
    host = "https://reqres.in"
    wait_time = constant(1)
    @task
    def hello_world(self):
        self.client.get("/api/users?page=2")
