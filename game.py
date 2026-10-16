import random

def guess_number():
    # 随机生成1~100之间整数
    answer = random.randint(1, 100)
    print("=====猜数字游戏=====")
    print("我已经想好了一个1到100之间的整数，你来猜猜！")
    count = 0
    while True:
        try:
            num = int(input("请输入你猜测的数字："))
            count += 1
            if num < answer:
                print("太小了！再试试")
            elif num > answer:
                print("太大了！再试试")
            else:
                print(f"恭喜你猜对啦！答案就是{answer}")
                print(f"你一共猜了{count}次")
                break
        except ValueError:
            print("输入无效！请输入整数！")

if __name__ == "__main__":
    guess_number()