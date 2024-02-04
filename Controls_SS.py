from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI

toys = scanner.find_toys()

print(toys)

#print("hi")

api1 = SpheroEduAPI(toys[0])
api1.spin(360, 1)

api2 = SpheroEduAPI(toys[1])
api1.spin(360, 1)

api1.spin(360, 1)

api2.spin(360, 1)

api1.spin(360, 1)