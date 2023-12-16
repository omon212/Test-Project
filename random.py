import time

def custom_random():
    current_time = int(time.time() * 10)
    return (current_time % 10) + 1

random_number = custom_random()
print(random_number)
