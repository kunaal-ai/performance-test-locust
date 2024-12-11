from locust import TaskSet, constant, task, HttpUser
'''
TaskSet
    - helps to structure the hierarchical 
    - can be nested
'''

class OneHttpCat(TaskSet):

    @task
    def get_status(self):
        self.client.get("/200")
        print("get status of 200")
        self.interrupt(reschedule=False)
        # interrupt - Signals the TaskSet to stop execution
        # reschedule=F - do not schedule immediately wait until next execution
        # if dont use Users never exits and get stuck where ever test execution begins

class TwoHttpCat(TaskSet):

    @task
    def get_500_status(self):
        self.client.get("/500")
        print("Get status 500")
        self.interrupt(reschedule=False)


class MyLoadTest(HttpUser):
    '''
    ~ this is the test runner just like python __main__, without this HttpUser - tests not found
    ~ should have tasks=[all above test case methods to run]
    ~ give host here will be considered as base-url for this file
    '''
    host = "https://http.cat"
    tasks = [OneHttpCat, TwoHttpCat]
    wait_time = constant(1)
