def main():
    # Calculate pay at work based on hours worked each day
    totalHour = 4 + 5 + 8 + 4
    salary = 8.75
    totalPay = totalHour * salary
    tax = 0.20
    print("My total hours worked:")
    print(totalHour)

    print("My hourly salary:")
    print(8.75)

    print("My total pay:")
    print(totalPay)

    print("My taxes owed:")  # 20% tax
    print(totalPay * tax)

main()