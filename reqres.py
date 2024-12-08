from locust import HttpUser, constant, task

class MyReqRes(HttpUser):

    host = "https://reqres.in"
    wait_time = constant(1)

    @task
    def get_user(self):
        res = self.client.get("/api/users?page=2")
        print(res.text)
        print(res.status_code)
        print(res.headers)

    @task
    def create_user(self):
        self.client.post("/api/users", data='''{
    "name": "morpheus",
    "job": "leader"
}''')

