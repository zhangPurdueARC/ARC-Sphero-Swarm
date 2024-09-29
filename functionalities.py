from spherov2 import scanner 
from spherov2.sphero_edu import SpheroEduAPI
import time
import matplotlib.pyplot as plt
import csv

# values for operation
toy_name = scanner.find_toy(toy_name = "SB-B11D")
speed = int(input("Speed of the ball: "))
heading = float(input("Heading: "))
operational_time = float(input("Number of seconds: "))

# place data gather values below
location_data = []
velocity_data = []
acceleration_data = []

orientation_data = []
gyroscope_data = []

time_data = []

with SpheroEduAPI(toy_name) as bolt:
    bolt.set_speed(speed)
    bolt.set_heading(heading)
    
    start_time = time.time()
    while (start_time + operational_time > time.time()):
        time_data.append(time.time())
        location_data.append(bolt.get_location())
        acceleration_data.append(bolt.get_acceleration())
        velocity_data.append(bolt.get_velocity())

        orientation_data.append(bolt.get_orientation())
        gyroscope_data.append(bolt.get_gyroscope())
        time.sleep(1)

print(location_data)
print(velocity_data)
print(acceleration_data)

x_loc = [loc_set["x"] for loc_set in location_data]
y_loc = [loc_set["y"] for loc_set in location_data]
# no z_loc

x_vel = [vel_set["x"] for vel_set in velocity_data]
y_vel = [vel_set["y"] for vel_set in velocity_data]
# no z_vel either

x_accel = [accel_set["x"] for accel_set in acceleration_data]
y_accel = [accel_set["y"] for accel_set in acceleration_data]
z_accel = [accel_set["z"] for accel_set in acceleration_data]

time_data = [moment-time_data[0] for moment in time_data]

# x values graphed
plt.plot(time_data, x_loc, label = "x")
plt.plot(time_data, x_vel, label = "x-velocity")
plt.plot(time_data, x_accel, label = "x-acceleration")
plt.xlabel("Time (s)")
plt.legend()
plt.show()

# y values graphed
plt.plot(time_data, y_loc, label = "x")
plt.plot(time_data, y_vel, label = "x-velocity")
plt.plot(time_data, y_accel, label = "x-acceleration")
plt.xlabel("Time (s)")
plt.legend()
plt.show()

print(orientation_data)
print(gyroscope_data)

pitch = [orientation_set["pitch"] for orientation_set in orientation_data]
yaw = [orientation_set["yaw"] for orientation_set in orientation_data]
roll = [orientation_set["roll"] for orientation_set in orientation_data]

pitch_vel = [gyro_set["pitch"] for gyro_set in gyroscope_data]
yaw_vel = [gyro_set["yaw"] for gyro_set in gyroscope_data]
roll_vel = [gyro_set["roll"] for gyro_set in gyroscope_data]

with open('functionalities.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # figure out a way to write in values into csv for easy comparison