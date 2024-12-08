from locust import User, task, constant

'''
~ Tests does not run in sequential order, so use weight

User
    - represents user that's about to attack system.
    - greenlet (just like threads)

HttpUser 
    - creates client (instances of https)
    - GET, POST, DELETE, PATCH, HEAD, PUT, headers, text, status_code etc.
    - variables: abstract = True, client = instance of HttpSession

HttpSession
    - handles cookies, maintains session state (login, authentication)
'''


class SimpleUser(User):
    """
        weight  -controls distribution of task
                - higher weight means, run more frequently
                - class based [weight = 2] / function based [ @task(2) ]
    """
    weight = 2
    wait_time = constant(1)
    @task(2)
    def launch(self):
        print("Launching the URL")

    @task
    def search(self):
        print("searching")


class ChildApp(User):
    weight = 2
    wait_time = constant(1)
    @task
    def select_item(self):
        print("selecting element")

    @task
    def checkout_out(self):
        print("payment in process")
