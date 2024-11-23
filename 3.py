# Question 3

# Employee Salary Management System

def calculate_salary():# calling function to calculate salary
    # Input the number of employees
    num_employees = int(input("Enter the number of employees: ")) 
    
    employees = [] #creating employee list
    
    for _ in range(num_employees): #creating for loop of employees performance, wage and bonus
        print("\nEnter details for employee:") 
        name = input("Employee Name: ")
        hours_worked = float(input("Number of hours worked in a week: "))
        hourly_rate = float(input("Hourly Rate: "))
        performance_rating = int(input("Performance Rating (1 to 5): "))
        
        # Calculate base salary
        base_salary = hours_worked * hourly_rate
        
        # Calculate bonus based on performance
        if performance_rating == 5:
            bonus = 0.20 * base_salary
        elif performance_rating == 4:
            bonus = 0.10 * base_salary
        elif performance_rating == 3:
            bonus = 0.05 * base_salary
        else:
            bonus = 0.0
        
        # Calculate overtime pay
        if hours_worked > 40:
            overtime_hours = hours_worked - 40
            overtime_pay = overtime_hours * (1.5 * hourly_rate)
        else:
            overtime_pay = 0.0
        
        # Calculate total weekly salary including bonus and overtime
        total_salary = base_salary + bonus + overtime_pay
        
        # Deduct tax if applicable
        if total_salary > 1000:
            tax = 0.10 * total_salary
        else:
            tax = 0.0
        
        # Net salary after tax
        net_salary = total_salary - tax
        
        # Store employee details
        employees.append({
            "name": name,
            "base_salary": base_salary,
            "bonus": bonus,
            "overtime_pay": overtime_pay,
            "tax": tax,
            "net_salary": net_salary
        })
    
    # Output individual employee details
    print("\nEmployee Salary Details:")
    for emp in employees:
        print(f"\nName: {emp['name']}")
        print(f"Base Salary: ${emp['base_salary']:.2f}")
        print(f"Bonus: ${emp['bonus']:.2f}")
        print(f"Overtime Pay: ${emp['overtime_pay']:.2f}")
        print(f"Tax Deducted: ${emp['tax']:.2f}")
        print(f"Net Salary: ${emp['net_salary']:.2f}")
    
    # Calculate overall summary
    total_payroll = sum(emp['net_salary'] for emp in employees)
    highest_paid_employee = max(employees, key=lambda emp: emp['net_salary']) #lambda calls a function in single line
    
    print("\nOverall Summary:")
    print(f"Total Payroll for the Company: ${total_payroll:.2f}")
    print(f"Highest Paid Employee: {highest_paid_employee['name']} with a salary of ${highest_paid_employee['net_salary']:.2f}")

# Run the program
if __name__ == "__main__":
    calculate_salary()
