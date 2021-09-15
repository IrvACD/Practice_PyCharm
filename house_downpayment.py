house_price = int(input("House price: "))
good_credit = True

if good_credit:
    downpayment = house_price * 0.1
else:
    downpayment = house_price * 0.2
print(f"Downpayment: ${downpayment}")