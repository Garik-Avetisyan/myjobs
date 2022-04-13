print(" ")
print("README: ays produkt@ naxatesvac e xanutneri kam pahestneri hamar. Skzbum karox eq mutqagrel <<buy, sell kam remainder>>")
print("remainder - cuyc e talis pahestum apranqi anun@, qanak@, mek hati mijin gin@:")
print("buy - grum eq gnvox apranqi anun@, qanak@, mek hati arjeq@")
print("sell - grum eq vacharvox apranqi anun@, qanak@, mek hati arjeq@")
print(" ")
class Warehouse:
    def __init__(self):
        self.productName = None
        self.quantity = 0
        self.price = 0
        self.remainder = []
        self.income = 0


    def inputProductName(self,):
        self.productName = input(" ENTER PRODUCT NAME ")
        self.quantity = int(input(" ENTER QUANTITY "))
        self.price = int(input(" ENTER PRICE "))


    def buy(self):
        a = 0
        newProduct = [self.productName, self.quantity, self.price]
        if len(self.remainder) > 0:
            for i in self.remainder:
                if i[0] == newProduct[0]:
                    i[1] = i[1] + newProduct[1]
                    i[2] = (i[2] + newProduct[2])/2
                    a += 1
            if a == 0:
                self.remainder.append(newProduct)
        else:
            self.remainder.append(newProduct)
        print("----------------------------------------------------")


    def sell(self):
        print("sell")
        a = 0
        if len(self.remainder) > 0:
            us1.inputProductName()
            for i in self.remainder:
                if self.productName == i[0]:
                    i[1] = i[1] - self.quantity
                    if i[1] < 0:
                        print(f"THERE IS NO {self.quantity} {i[0]} IN STOCK, YOUR RESIDUE IS {i[1] + self.quantity} PIECES")
                        i[1] = i[1] + self.quantity
                        a += 1
                    else:
                        self.income += (self.price-i[2]) * self.quantity
                        a += 1
            if a == 0:
                print(f"NO {self.productName} IN STOCK")
            print("----------------------------------------------------")
            print(f"NET PROFIT {self.income}")
            print("----------------------------------------------------")


        else:
            print("YOUR WAREHOUSE IS EMPTY")


    def remainderr(self):
        print(f"remaining products in stock <<name,quantity,price>> {self.remainder}")
        print("----------------------------------------------------")


    def start(self):
        x = 1
        while x == 1:
            a = input("What do you want to do ? ")
            if a == "buy":
                self.inputProductName()
                self.buy()
            elif a == "sell":
                self.sell()
            elif a == "remainder":
                self.remainderr()
            else:
                print("WRONG INPUT: << please input buy,sell or remainder >>")
                print("----------------------------------------------------")






us1 = Warehouse()
us1.start()


