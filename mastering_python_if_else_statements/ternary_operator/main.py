water_intake = 1.5  # Example value
true_message = "You've met your hydration goal!"
false_message = "Drink more water to reach your goal."

# Using ternary operator to check hydration goal
message = true_message if water_intake >= 2.0 else false_message

# Testing
print("Hydration Status:", message)

#steps_taken = 8500
#status = ""

#if steps_taken >= 10000:
#    status = "Goal Reached"
#else:
 #   status = "Keep Going"

#print(status)

#steps_taken = 8500
#status = "Goal Reached" if steps_taken >= 10000 else "Keep Going"

#print(status)
