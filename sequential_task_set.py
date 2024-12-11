from locust import SequentialTaskSet, HttpUser, constant, user, task

class MySeqTask(SequentialTaskSet):

    @task
    def get_status(self):
        self.client.get("/200")
        print("status of 200")

    @task
    def get_500_status(self):
        self.client.get("/500")
        print("status of 500")


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks = [MySeqTask]
    wait_time = constant(1)