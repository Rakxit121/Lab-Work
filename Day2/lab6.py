# running faster or bus
distance = 9
speed_on_bus = (9/25)*60
total_time_bus = speed_on_bus*20

speed_walking_A = (1/7)*60
speed_walking_B= (2/15)*60
speed_walking_C = (1/7)*60

total_time_walking = speed_walking_A+speed_walking_B+speed_walking_C

print("the total time taken by bus is : " , total_time_bus)
print("the total time taken by walking is : " , total_time_walking)

if total_time_walking>total_time_bus:
    print("walking is faster than bus")
else:
    print("bus is faster than walking")