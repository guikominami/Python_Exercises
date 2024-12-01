#https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34583410#overview

velocity = [60, 60, 60, 62, 63]
local_car_km = [99, 100, 101, 98, 102]

RADAR = 60
LOCAL_RADAR_KM = 100
RADAR_RANGE = 1

limit_radar_min = LOCAL_RADAR_KM - RADAR_RANGE
limit_radar_max = LOCAL_RADAR_KM + RADAR_RANGE
velocity_car_when_pass_radar = velocity > RADAR
car_position1 = local_car_km >= (limit_radar_min)
car_position2 = local_car_km <= (limit_radar_max)

if velocity_car_when_pass_radar and (car_position1 and car_position2):
    print("Car velocity is upper than the limit! Car was fined!")