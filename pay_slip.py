#Ibet Abdul-muhssin Jabir

#Constant Variables declaration
total_slips = 0
net_pay = 0
total_net_pay = 0.0
highest_net_pay = -1.0
highest_paid_name = "none"
TAX_RATE = 0.0
PENSION_RATE = 0.0

print("-------payroll processing system")
#initializing while loop
while True:
    employee_name = input("enter employee name: ").strip()
    if not employee_name:
        print("employee name cannot be empty.")
        continue

    hours = float(input("enter hours worked: "))
    rate = float(input("enetr hourly rate: "))
    TAX_RATE = float(input("enter tax rate: "))
    PENSION_RATE  = float(input("enter pension rate: "))
    ValueError 

    print("invalid numeric input. skipping this employee.")

    if hours < 0 or hours > 300 or rate <= 0:
        print("invalid entry")
        continue

    regular_hours = min(hours, 160)
    overtime_hours = max(hours - 160, 0)
    regular_pay = regular_hours * TAX_RATE
    overtime_pay = overtime_hours * TAX_RATE * 1.5
    gross_pay = regular_pay + overtime_pay

    tax_amount = gross_pay * TAX_RATE
    pension_amount = gross_pay * PENSION_RATE
    net_pay = gross_pay - tax_amount - pension_amount
    if gross_pay == 24000:
        print(tax_amount)
        tax_amount = 0.01*gross_pay
        if gross_pay == 8000:
            print(tax_amount)
            tax_amount = 0.25 *gross_pay
            if gross_pay == 6000:
             print(tax_amount)
             tax_amount == 0.30 *gross_pay


    print(f"employee name: {employee_name}")
    print(f"gross pay: {gross_pay:.2f}")
    print(f"tax: {tax_amount:.2f}")
    print(f"pension: {pension_amount:.2f}")
    print(f"net pay: {net_pay:.2f}")

    total_slips += 1
    total_net_pay += net_pay

    if net_pay > highest_net_pay:
        highest_net_pay = net_pay
        highest_paid_name = employee_name

    another = input("do you wish to add another employee? (yes/no): ").strip().lower()
    if another != "yes":
        break
print("\n" + "= " * 15 +"\n")
print("\npayroll summary report")
print(f"total payslips processed: {total_slips}")
print(f"total net pay: {total_net_pay:.2f}")
print(f"highest net pay: {highest_net_pay:.2f}")
print(f"employee with highest pay: {highest_paid_name}")
print("\n" + "= " * 15 +"\n")


  
   
 