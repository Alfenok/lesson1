def format_price(price):
    price = int(float(price))
    return f"Цена: {price} руб."

print(format_price("56.24"))