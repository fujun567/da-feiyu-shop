products = {
    "奶茶":18,
    "炸鸡":30,
    "甜品":25,
    "羽毛球拍":200,
    "Python教程":59
}
SPORTS_ITEM = {"羽毛球拍"}

THRESHPLD = 100
RATE = 0.9
cart = []

def show_menu():
    print("\n==== 大肥鱼专属商城 ====")
    print("1.查看商品库")
    print("2.添加商品到购物车")
    print("3.查看购物车")
    print("4.结算并清空购物车")
    print("5.退出系统")

def add_to_cart():
    item = input("请输入要购买的商品名称：").strip()
    if item in products:
        cart.append(item)
        print(f"✅成功将[{item}]加入购物车！")
    else:
        print("❌商品不存在,请检查输入是否正确!")

def view_cart():
    if  not cart:
        print("🛒购物车空空如也，大肥鱼你还没买东西！")
        return 0
    print("\n--- 当前购物车 ---")
    total = 0
    for item in cart:
        price = products[item]
        total += price
        print(f"- {item}:￥{price}")
    print(f"💰总计：￥{total}")
    return total

def calc_payable():
    discountable = sum(products[i] for i in cart if i not in SPORTS_ITEM)
    sports= sum(products[i] for i in cart if i in SPORTS_ITEM)
    discount = round(discountable * (1 - RATE),2) if discountable >= THRESHPLD else 0
    payable = round(discountable + sports - discount,2)
    return discountable,sports,discount ,payable
 

def checkout():
    if not cart:
        print("购物车里是空的,无法结算！")
        return
    
    view_cart()
    discountable,sport,discount ,payable = calc_payable()
    print("\n---- 结算明细 ----")
    print(f"可打折商品合计:￥{discountable}")
    print(f"体育用品合计：{sport}(不参与打折)")
    if discount > 0:
        print(f"🎉可打折部分满(THRESHPLD)，打九折，优惠 ￥{discount}")
    else:
        print(f"可打折部分未满(THRESHOLD)，不打折")
    print(f"最终结算金额：￥{payable}")

    cart.clear()
    print("✅结算完成，购物车已清空！")

while True:
    show_menu()
    choice = input("请选择操作(1-5):").strip()

    if choice == "1":
        print("\n--- 商品库 ---")
        for name,price in products.items():
            print(f"{name}:￥{price}")
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        view_cart()
    elif choice == "4":
        checkout()
    elif choice == "5":
        print("退出系统,大肥鱼记得还债！")
        break
    else:
        print("❌输入错误,请输入1-5之间的数字。")