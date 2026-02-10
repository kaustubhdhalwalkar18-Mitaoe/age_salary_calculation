from datetime import datetime

# Read inputs
birth_date = input("Enter birth date (DD-MM-YYYY): ")
salary = float(input("Enter salary (in local currency): "))
conversion_rate = float(input("Enter conversion rate to dollars: "))

# Convert birth date string to date object
birth_date_obj = datetime.strptime(birth_date, "%d-%m-%Y")
today = datetime.today()

# Calculate age
age = today.year - birth_date_obj.year
if (today.month, today.day) < (birth_date_obj.month, birth_date_obj.day):
    age -= 1

# Convert salary to dollars
salary_in_dollars = salary * conversion_rate

# Output
print("\nEmployee Details")
print("----------------")
print(f"Age: {age} years")
print(f"Salary in Dollars: ${salary_in_dollars:.2f}")
