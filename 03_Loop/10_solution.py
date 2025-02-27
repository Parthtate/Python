import time

wait_time = 1
max_retries = 5
attempt = 0

while attempt < max_retries:
    print("ATTEMPT: ", attempt, "- WAIT TIME", wait_time,"Sec")   
    
    # ADD TIME EXPOENTIALLY WITH THE HELP OF TIME
    time.sleep(wait_time)
    wait_time = wait_time * 2
    # wait_time *= 2
    attempt += 1
