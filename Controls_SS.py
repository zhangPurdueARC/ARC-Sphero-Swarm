from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI

# Find toys
toys = scanner.find_toys(toy_names = ["SB-76B3", "SB-B11D"])

print(toys)

for toy in toys:
    with SpheroEduAPI(toy) as api:
        api.roll(0, 255, 1)