exercise_time = 8 # Example value for total exercise time in hours
title = ""

if exercise_time > 10:
    title = "Super Achiever"
elif exercise_time >= 6 and exercise_time <= 10: 
    title = "Hard Worker"
elif exercise_time >= 3:
    title = "Getting There"
else:
    title = "Needs Improvement"

# Testing
print("Your fitness level:", title)