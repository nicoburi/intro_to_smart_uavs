from drones import Drone

fuel = 100
max_speed = 120
refuel_quantity = 100
drone = Drone(fuel, max_speed)
###
print ('Current fuel is '+str(drone.get_fuel()))
print ('Current speed is '+str(drone.get_speed()))
drone.add_fuel(refuel_quantity)
print('Now the fuel is '+str(drone.get_fuel()))
drone.set_speed(111)
print ('Current speed is '+str(drone.get_speed()))
drone.fly()
