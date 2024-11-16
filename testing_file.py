from spherov2 import scanner 
from spherov2.sphero_edu import SpheroEduAPI
import time

def move_lengths(lengths, bolt):
    move_time = lengths * 2
    bolt.roll(0, 100, lengths)

def turn_routes(routes, bolt):
    routes
    bolt.spin(60 * routes, 2)

toy_name = scanner.find_toy(toy_name = "SB-1840")

# movement time between + start up time
op_time = 0.25 + 0.4

with SpheroEduAPI(toy_name) as bolt:
    move_lengths(1, bolt)
    turn_routes(1, bolt)
    move_lengths(2, bolt)
    time.sleep(3)
    # bolt.roll(60, 50, op_time)