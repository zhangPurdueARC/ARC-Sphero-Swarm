from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color
import threading
import time

def control_toy(toy, id):
    print(id)
    with SpheroEduAPI(toy) as api:
        choosenColor = Color(r = 255, g = 0, b = 0)
        api.set_front_led(choosenColor)
        api.set_back_led(choosenColor)
        # still needs more work (untested, also probably doesn't work on matrix)
        while True:    
            print(commands[id][0])
            if (commands[id][0] == "%"):
                break
            elif (commands[id][0] == "m"):
                api.roll(0, 255, 0.1)
            # probably need to graph sphero turning in order to get a good idea of what the rotate command should be
            else:
                print(commands[id][0] + "is an invalid command!")
            time.sleep(0.1)
            commands[id] = commands[id][1:]

def run_toy_threads(toys):
    threads = []
    global commands 
    commands = []
    for toy in toys:
        commands.append(["a"], ["b"], ["c"], ["d"], ["%"]) # matrix is needed for more complex commands
    id = 0
    for toy in toys:
        thread = threading.Thread(target=control_toy, args=[toy, id])
        threads.append(thread)
        thread.start()
        id += 1
    # while True: need to recieve commands in constantly updating format
    for thread in threads:
        thread.join()
    print("Ending function...")

# Find toys
toys = scanner.find_toys(toy_names = ["SB-76B3", "SB-B11D"])

print(toys)

run_toy_threads(toys)