import redis
from datetime import datetime

# class ActivityPlayer:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#         self.rank = -1
#
#     def setRank(self, rank):
#         self.rank = rank
#
#     def getRank(self):
#         return self.rank


class ActivityRanking:
    def __init__(self):
        self.rdb = redis.Redis(host='127.0.0.1', port=6379, password='123456')
        # self.players = {}
        # self.monthlyScore = 0

    def addPlayer(self, playerName, score):
        # 在每月活动中，玩家得到的活动总分为 0 到 10000 之间的整数
        month = datetime.now().month
        key = 'players_%s' % month
        self.rdb.zincrby(name=key, amount=score, value=playerName)
        # print('addPlayer  ', self.rdb.zrevrange(key, 0, -1))
        # self.players[playerName] = ActivityPlayer(playerName, score)
        # self.monthlyScore += score

    def getPlayerRank_10(self, playerName, month):
        # 系统提供玩家名次查询接口，玩家能够查询自己名次前后10位玩家的分数和名次
        # month = datetime.now().month
        key = 'players_%s' % month
        cc = self.rdb.zrevrank(key, playerName)
        t = 10
        start = cc - t
        if start < 0:
            start = 0
        end = cc + t
        withscore = self.rdb.zrevrange(key, start, end, withscores=True)

        print('withscore  3  ', withscore)
        s = 0
        res_list = []
        for i in withscore:
            s += 1
            print('玩家昵称  ', str(i[0]), ' 玩家分数  ', int(i[1]), '  玩家名次 ', start + s)
            res_list.append(['玩家昵称', str(i[0]), '玩家分数', int(i[1]), '玩家名次', start + s])
        # return self.players[playerName].getRank()
        return res_list
# 测试代码

ranking = ActivityRanking()
ranking.addPlayer("Alice", 500)
ranking.addPlayer("Bob", 300)
ranking.addPlayer("Charlie", 400)
ranking.addPlayer("Dave", 200)
ranking.addPlayer("Dave", 200)
# print(ranking.getPlayerRank_10("Alice")) # 输出: 1
# print(ranking.getPlayerRank_10("Bob")) # 输出: 2
# print(ranking.getPlayerRank_10("Charlie")) # 输出: 1
print(ranking.getPlayerRank_10("Dave", 9))  # 输出: 3

# 每月 。。。OK
# github
# 0-10000
# 多位一样，按照获取顺序
