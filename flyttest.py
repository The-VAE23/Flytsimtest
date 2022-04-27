import time
from flyt_python import api

drone = api.navigation(timeout = 1000000)       #Create Drone object

time.sleep(5)                                   #Wait for interface to initialize

print("Taking off, Target height 5m")
drone.take_off(5)                               #Take=off to an altitude of 5m

print("Tracing square with side length 6.5m")
drone.position_set(6.5, 0, 0, relative=True)    #Relative to current position move north 6.5m
drone.position_set(0, 6.5, 0, relative=True)    #Relative to current position move east 6.5m
drone.position_set(-6.5, 0, 0, relative=True)   #Relative to current position move south 6.5m
drone.position_set(0, -6.5, 0, relative=True)   #Relative to current position move west 6.5m

print("Landing at current position")
drone.land(async=False)                         #Land at current postion

drone.disconnect()                              #Disconnect from drone