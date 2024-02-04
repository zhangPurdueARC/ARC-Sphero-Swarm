from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
import threading
import time

def rotate_toy(toy):
    with SpheroEduAPI(toy) as api:
        api.roll(0, 255, 1)

def run_toy_threads(toys):
    threads = []
    for toy in toys:
        thread = threading.Thread(target=rotate_toy, args=[toy])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

# Find toys
toys = scanner.find_toys(toy_names = ["SB-76B3", "SB-B11D"])

print(toys)

run_toy_threads(toys)