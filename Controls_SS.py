from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI

# Find toys
toy = scanner.find_toy(toy_name = "SB-76B3")

print(toy)

with SpheroEduAPI(toy) as api:
    api.roll(0, 255, 1)