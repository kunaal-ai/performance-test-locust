# Performance Test - Locust

# single file run 
```locust -f file_name.py```

# all test run 
```locust```

# base-url 
1. in python file
2. cmd ```locust file_name.py --host=https://sample.com```

# Variables 
### User class
    - abstract = True
    - on_start()
    - on_stop()
    - tasks
    - wait()
    - wait_time()
    - weight = 10

### HttpUser
    - abstract = True
    - client = instance

### TaskSet - can be nested
    - client
    - interrup
    - on_start()
    - on_stop()
    - parent
    - tasks
    - user
    - wait()
    - wait_time()


