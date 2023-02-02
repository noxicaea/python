import hashlib
import time

class Member:
    def __init__(self, name, passwd,card,integral,redate):
        self.name = name
        self.passwd = passwd
        self.card = card
        self.integral = integral
        self.redate = redate

class PasswdMixin:
    def too_short(self, passwd):
        while len(passwd) < 6:
            passwd = input("密码太短，请重新输入：")
        return passwd
    def to_md5(self,passwd):
        passwd = hashlib.md5(passwd.encode()).hexdigest()
        return passwd

class LoggerMixin:
    def log(self, msg):
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write(msg + "\n")

class Manage(PasswdMixin,LoggerMixin):
    def __init__(self):
        self.cards = 10000
        self.registered = {}
    
    def main(self):
        while True:
            print(self.registered)
            print("欢迎来到超市会员管理系统".center(30, '-'))
            print("1.创建新卡;2.修改密码;3.商品支付;4.积分查询;5.退出程序：",end="")
            nums = input()
            if nums == "1":
                self.create_card()
            elif nums == "2":
                self.change_passwd()
            elif nums == "3":
                self.pay()
            elif nums == "4":
                self.query()
            elif nums == "5":
                sure = input("确定要退出吗？(y/n)")
                if sure == "y":
                    break
                elif sure == "n":
                    continue
                else:
                    print("输入有误")
            else:
                print("输入有误")
    
    def create_card(self):
        name = input("请输入姓名：")
        passwd = input("请输入密码：")
        passwd = self.too_short(passwd)
        passwd = self.to_md5(passwd)
        card = self.cards
        integral = 0
        redate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        member = Member(name, passwd, card, integral, redate)
        self.registered[card] = member
        print(f"注册成功，您的用户名为：{name} 您的卡号为：{card}")
        self.cards += 1
        self.log("卡号：{} 注册成功，时间：{}".format(card,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    
    def change_passwd(self):
        cardid = int(input("请输入卡号："))
        passwd = input("请输入密码：")
        if cardid in self.registered.keys():
            if self.registered[cardid].passwd == self.to_md5(passwd):
                print("密码正确")
                self.registered[cardid].passwd = input("请输入新密码：")
                self.registered[cardid].passwd = self.too_short(self.registered[cardid].passwd)
                self.registered[cardid].passwd = self.to_md5(self.registered[cardid].passwd)
                print("卡号：{} 修改成功，时间：{}".format(cardid,time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
                self.log("卡号：{} 修改成功，时间：{}".format(cardid,time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
            else:
                print("密码错误")
        else:
            print("卡号不存在")
    
    def pay(self):
        cardid = int(input("请输入卡号："))
        passwd = input("请输入密码：")
        if cardid in self.registered.keys():
            if self.registered[cardid].passwd == self.to_md5(passwd):
                print("密码正确")
                money = int(input("请输入金额："))
                self.registered[cardid].integral += money
                print("卡号：{} 本次消费：{}，累计积分为：{}，时间：{}".format(cardid,money,self.registered[cardid].integral,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
                self.log("卡号：{} 本次消费：{}，累计积分为：{}，时间：{}".format(cardid,money,self.registered[cardid].integral,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
            else:
                print("密码错误")
        else:
            print("卡号不存在")
    
    def query(self):
        cardid = int(input("请输入卡号："))
        passwd = input("请输入密码：")
        if cardid in self.registered.keys():
            if self.to_md5(passwd) == self.registered[cardid].passwd:
                print("密码正确")
                print("卡号：{} 当前积分为：{}，时间：{}".format(cardid,self.registered[cardid].integral,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
            else:
                print("密码错误")
        else:
            print("卡号不存在")
m = Manage()
m.main()