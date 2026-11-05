"""問題 ： 野菜の収穫チェック
①野菜を Yasai クラスで作成(トマト 収穫まで30日、ナス 収穫まで25日)
②日にちを進めるメソッドを作る(何日進めるか選べるようにする)
③今日は何日目か確認するメソッドを作る「~は育てて◯日目です」と出力
④収穫できるか調べるメソッドを作る。収穫日数に達していれば「〜は収穫できます!」、
そうでなければ「〜はまだ収穫できません」と出力
⑤トマトとナスの日にちを20日目にして、様子を見て、収穫できるか調べる。さらに5日進めて、
もう一度様子を見て、収穫できるか調べる
"""


class Vegetable:
    def __init__(
        self,
        name,
        harvest,
    ):
        self.name = name
        self.harvest = harvest
        self.days = 0

    def day_count(self, day):
        self.days += day

    def check_day(self):
        print(f"{self.name}は育てて{self.days}日目です")

    def check_harvest(self):
        if self.days >= self.harvest:
            print(f"{self.name}は収穫できます!")
        else:
            print(f"{self.name}はまだ収穫できません")


vegetables = [Vegetable("トマト", 30), Vegetable("ナス", 25)]
for vegetable in vegetables:
    vegetable.day_count(20)
    vegetable.check_day()
    vegetable.check_harvest()

for vegetable in vegetables:
    vegetable.day_count(5)
    vegetable.check_day()
    vegetable.check_harvest()
