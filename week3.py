def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
        amount = price - (price *(discount_percent/100))
        return amount
    else:
        price

#Get inputs
price = float(input("Enter the price here: "))  
discount_percent = float(input("Enter the discount percentage: "))   

#Price
finalprice = calculate_discount(price,discount_percent)

print(f'You should pay: {finalprice:.2f} thank you')

