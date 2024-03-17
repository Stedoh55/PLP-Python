def calculate_discount(price, discount_percent):
    price = float(input('What is the item price?'))
    discount_percent = float(input('What is discount percentage?'))

    if discount_percent >= 20:
        discount = price - (discount_percent/ 100) * price
        print(discount)
    else:
        print(price)
calculate_discount(1000,20)