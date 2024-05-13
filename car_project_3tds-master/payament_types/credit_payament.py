from payament_times.in_time import *
from payament_types.nine_mounths import *
from payament_types.six_mounths import *
from payament_types.three_mounths import *
from payament_types.twelve_payament import *

def credit_payament(desired_car, time_option):
    if(time_option == 1):
        return (in_time(desired_car))
    elif(time_option == 2):
        return (three_mounths(desired_car))
    elif(time_option == 3):
        return (six_mounths(desired_car))
    elif(time_option == 4):
        return (nine_mounths(desired_car))
    elif(time_option == 5):
        return (twelve_mounths(desired_car))

