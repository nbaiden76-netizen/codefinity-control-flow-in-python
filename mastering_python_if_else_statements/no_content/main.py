password = "user123"
correct_password = "p@ssword123"

login_message = "Login sucessful!" if password == correct_password else "Incorrect password, try again."

# Testing
print("Login Status:", login_message)