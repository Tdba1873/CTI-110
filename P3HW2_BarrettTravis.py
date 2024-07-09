# Travis Barrett
# 09 Jul 2024
# P3HW2
# This project will calculate an employees's pay

name = input("Enter the employee's name: ")
hoursWorked = float(input("Enter number of hours worked: "))
payRate = float(input("Enter employee's pay rate: "))
print("-------------------------------------")

if hoursWorked > 40:
    # calculate overtime
    ovtHours = hoursWorked - 40
    # Calculate overtime pay
    ovtPay = ovtHours * (payRate * 1.5)
    # Calculate pay for regular hours
    regPay = 40 * payRate
    # calculate gross pay
    grossPay = regPay + ovtPay

else:
    # set over time hours and pay to zero
    ovtHours = 0
    ovtPay = 0
    regPay = payRate * hoursWorked
    grossPay = regPay


print("Employee name: ",name,"\n")

print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"Overtime Pay":<20}{"RegHour Pay":<20}{"Gross Pay":}')
print ("-"*98)
print(f'{hoursWorked:<15}{payRate:<12}{ovtHours:<12}{ovtPay:<20.2f}{"$"}{regPay:<20.2f}{"$"}{grossPay:.2f}')




