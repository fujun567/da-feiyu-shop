def calculate_debt(origanal_price,discount=0.9):
    final_price = origanal_price * discount
    return round(final_price,2)

print(f"大肥鱼欠我奶茶,炸鸡和甜品,原价200,打完折后：{calculate_debt(200)}")