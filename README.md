# Performance Test - Locust

# single file run 
```locust -f file_name.py```

# all test run 
```locust```

# base-url 
1. in python file
2. cmd ```locust file_name.py --host=https://sample.com```

# Tags
```--tags tag_name```
```--exclude-tags tag_name```

# Summary
```--only-summary```

# correlation
    1. extracting dynamic value from response
    2. pass extracted value in other requests
        e.g: session id [login token], order numbers, customer id

# Classes and Variables 
### User class
    ~ represents user that's about to attack system.
    ~ greenlet (just like threads)

    - abstract = True
    - on_start() -> when user starts [before]
    - on_stop() -> when user stops [after]
    - tasks
    - wait()
    - wait_time()
    - weight = 10

### HttpUser
    ~ creates client (instances of https)
    ~ GET, POST, DELETE, PATCH, HEAD, PUT, headers, text, status_code etc.
    
    - abstract = True
    - client = instance of HttpSession

### TaskSet 
    ~ can be nested 
    ~ to structure the hierarchical 
    
    - client
    - interrupt
    - on_start() -> when taskset start
    - on_stop() -> when taskset stops
    - parent
    - tasks
    - user
    - wait()
    - wait_time()

### SequentialTaskSet
    ~ tasks executed in sequential order
    ~ weight attribute - ignored

    - client
    - interrupt(reschedule=True)
    - on_start()
    - on_stop()
    - parent
    - schedule_task(task_callable, first=False)
    - user
    - wait_time()

# Variables Def
### wait_time(seconds)
    1. between(min, max) # random sleep
    2. constant(wait_time) # fixed sleep
    3. constant_pacing(wait_time) 
           ~ Ensures that each iteration of tasks (task execution + wait) takes at least wait_time seconds.
           ~ If task finishes early, remaining time is added as sleep. If the task takes longer, no additional wait time.
           ~ ```wait_time = constant_pacing(5)``` Ensures task + wait takes at least 5 seconds
           ~ If a task completes in 2 seconds, the user waits for 3 seconds (total = 5s).
           ~ If a task takes 6 seconds, the user doesn’t wait and moves to next task.

# Command Line Options
    - Runtime
    - stats
    - log
    - Web UI
    - Master and Worker
    - Tag
    - Others

        - locust -h
        - locust -f file_name.py -l -u 1 -r 1 -t 10s --headless --print-stats 
            --csv Run1.csv --csv-full-history --host=https://example.com 
            -L CRITICAL --logfile mylog.log --html test_report.html
        
            - locust -f file_name.py --show-task-ratio 
                ~ prints the task execution ratio on terminal
                ~ can be printed in json --show-task-ratio-json
            ~ l = list all users
            ~ u = users
            ~ r = respond rate
            ~ t = time
            ~ L = log [DEBUG, INFO, WARNING, ERROR, CRITICAL]
        
# Response Validation

    1. catch_response=True
    2. response.success()
    3. response.failure()
