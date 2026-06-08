# Student Grade Calculator

# Function to calculate grade and message
def calculate_grade(marks):

    if marks >= 90:
        return "A", "Excellent Work! You are amazing! 🌟"

    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"

    elif marks >= 70:
        return "C", "Good Job! You can do even better! 😊"

    elif marks >= 60:
        return "D", "Nice effort! Keep practicing! 📚"

    else:
        return "F", "Don't give up! Keep learning and improving! 💪"


# Get student name
student_name = input("Enter student name: ")

# Input validation using while loop
while True:

    try:
        marks = int(input("Enter marks (0-100): "))

        if 0 <= marks <= 100:
            break

        else:
            print("❌ Invalid input! Marks must be between 0 and 100.")

    except ValueError:
        print("❌ Please enter a valid number.")


# Calculate grade
grade, message = calculate_grade(marks)

# Display result
print("\n📊 RESULT FOR", student_name.upper() + ":")
print("Marks:", marks, "/100")
print("Grade:", grade)
print("Message:", message)
