# Distance to the destination in miles
distance_mi = 0
# Current weather condition
is_raining = False

# Available transportation options
has_bike = False
has_car = True
has_ride_share_app = True

# If the distance is a falsy value (0), print False
if not distance_mi:
    print("False")

# If the destination is 1 mile or less and it isn't raining, print True
elif distance_mi <= 1 and not is_raining:
    print("True")

# If the distance is more than 1 mile but no more than 6 miles,
# a bike is available, and it isn't raining, print True
elif distance_mi > 1 and distance_mi <= 6 and has_bike and not is_raining:
    print("True")

# If the distance is more than 6 miles and a ride-share app is available,
# print True
elif distance_mi > 6 and has_ride_share_app:
    print("True")

# If the distance is more than 6 miles and a car is available,
# print True
elif distance_mi > 6 and has_car:
    print("True")

# If none of the above conditions are met, print False
else:
    print("False")