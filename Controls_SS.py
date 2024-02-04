from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
import threading
import time

def control_toy(toy, id):
    print(id)
    with SpheroEduAPI(toy) as api:
        while commands[id] != "":    
            api.roll(0, 255, 1)
            print(commands[id])
            commands[id] = commands[id][1:]
            time.sleep(0.1)

def run_toy_threads(toys):
    threads = []
    global commands 
    commands = []
    for toy in toys:
        commands.append("abcd")
    id = 0
    for toy in toys:
        thread = threading.Thread(target=control_toy, args=[toy, id])
        threads.append(thread)
        thread.start()
        id += 1
    for thread in threads:
        thread.join()
    print("Ending function...")

# Find toys
toys = scanner.find_toys(toy_names = ["SB-76B3", "SB-B11D"])

print(toys)

run_toy_threads(toys)