# Exponential Backoff strategy
import time
wait_time = 1
max_retries = int(input("Enter the number of retires: "))
attempts = 0
while attempts < max_retries:
    print(f"Attempt {attempts + 1} - wait time {wait_time}")
    time.sleep(wait_time)
    wait_time = wait_time * 2
    attempts += 1
