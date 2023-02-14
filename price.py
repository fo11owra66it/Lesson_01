def format_price(price):
    price = int(price)
    return f'Цена: {price} руб.'

total_price = format_price(56.24)
print(total_price)