from locust import HttpUser, task, constant
'''
run this using cmd 
locust -f file_name.py -u 1 -r 1 -t 10s --headless --print-stats 
            --csv Run1.html.csv --csv-full-history --host=https://example.com
'''

class MyLoadTest(HttpUser):

    wait_time = constant(1)

    @task
    def launch(self):
        self.client.get("/")