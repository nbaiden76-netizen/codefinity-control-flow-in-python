steps_taken = 9000
step_goal = 10000
calories_burned = 350
calorie_goal = 500
morning_exercise = False

all_conditions_met = True

# Rewrite this using a single if statement
if (steps_taken <= step_goal) and (calories_burned <= calorie_goal) and (morning_exercise == False):
    all_conditions_met = False
   

# Testing
print("Have all conditions been met?", all_conditions_met)

# Example 1: AND has higher precedence than OR
#steps_taken = 8000
#step_goal = 10000
#calories_burned = 450
#calorie_goal = 500

#first_result = steps_taken >= step_goal or calories_burned >= calorie_goal and False
# Same as: steps_taken >= step_goal or (calories_burned >= calorie_goal and False)

# Example 2: Parentheses change the precedence
# second_result = (steps_taken >= step_goal or calories_burned >= calorie_goal) and True

# Example 3: NOT has the highest precedence
# third_result = not (steps_taken >= step_goal) or calories_burned >= calorie_goal
# Same as: (not (steps_taken >= step_goal)) or (calories_burned >= calorie_goal)

#print('The first expression is:', first_result)
#print('The second expression is:', second_result)
#print('The third expression is:', third_result)

