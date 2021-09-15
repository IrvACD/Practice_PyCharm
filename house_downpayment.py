house_price = int(input("House price: "))
good_credit = True

if good_credit:
    down_payment = house_price * 0.1
else:
    down_payment = house_price * 0.2
print(f"Downpayment: ${down_payment}")