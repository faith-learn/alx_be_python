# daily_reminder.py

# 1. Prompt for a single task
task = input("Enter your task: ")

# 2. Prompt for the task's priority
priority = input("Priority (high/medium/low): ")

# 3. Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ")

# Process the task based on priority using a match-case statement
match priority.lower():
    case 'high':
        reminder_text = "a high priority task"
    case 'medium':
        reminder_text = "a medium priority task"
    case 'low':
        reminder_text = "a low priority task. Consider completing it when you have free time."
    case _:
        # Default case if the input is not 'high', 'medium', or 'low'
        reminder_text = "a task"

# Use an if statement to modify the reminder for time-bound tasks
if time_bound.lower() == 'yes':
    print(f"Reminder: '{task}' is {reminder_text} that requires immediate attention today!")
else:
    print(f"Note: '{task}' is {reminder_text}")