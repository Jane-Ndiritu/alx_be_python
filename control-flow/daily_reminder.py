task = input ("Enter your task:")   
priority = input ("priority (high/medium/low):")
time = input("Is it time-bound? (yes/no): ")
if priority.lower() == "high" and time.lower() == "yes":
    print(f"Reminder: Your high-priority task '{task}' is time-bound. Please address it immediately!")  
elif priority.lower() == "high":
    print(f"Reminder: Your high-priority task '{task}' needs your attention soon.")         
elif priority.lower() == "medium":
    print(f"Reminder: Your medium-priority task '{task}' should be completed in due time.")
elif priority.lower() == "low":
    print(f"Reminder: Your low-priority task '{task}' can be done at your convenience.")
else:
    print("Invalid priority level. Please enter high, medium, or low.")