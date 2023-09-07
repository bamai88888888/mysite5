import time

import redis
from datetime import datetime
import random


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
        # self.rdb = redis.Redis(host='127.0.0.1', port=6379, password='123456')
        self.players = {}
        self.players2 = {}
        self.monthlyScore = 0
        self.sortedPlayers = []

    def addPlayer(self, playerName, score):
        # 在每月活动中，玩家得到的活动总分为 0 到 10000 之间的整数
        # month = datetime.now().month
        # key = 'players_%s' % month
        # self.rdb.zincrby(name=key, amount=score, value=playerName)
        # print('addPlayer  ', self.rdb.zrevrange(key, 0, -1))
        # self.players[playerName] = ActivityPlayer(playerName, score)
        self.players[playerName] = [self.players.get(playerName, [0, 0, playerName, -1])[0] + score, time.time(), playerName, -1]  # ActivityPlayer(playerName, score)
        # self.monthlyScore += score

    def addPlayer_40w(self):
        # 在每月活动中，玩家得到的活动总分为 0 到 10000 之间的整数
        month = datetime.now().month
        key = 'players_%s' % month
        # self.rdb.zincrby(name=key, amount=score, value=playerName)
        for i in range(400000):
            score = random.randint(1, 1000)
            self.addPlayer(i, score)
            # self.rdb.zincrby(name=key, amount=score, value=i)
        # print('addPlayer  ', self.rdb.zrevrange(key, 0, -1))
        # self.players[playerName] = ActivityPlayer(playerName, score)
        # self.monthlyScore += score

    def calculateMonthlyRanking(self):
        # sortedPlayers = sorted(self.players.values(), key=lambda x: (-x.score, x.name))
        sortedPlayers = sorted(self.players.values(), key=lambda x: (-x[0], x[1]))
        print('sort  ', sortedPlayers)
        for i in range(len(sortedPlayers)):
            #     sortedPlayers[i].setRank(i + 1)
            sortedPlayers[i][3] = i+1
            self.players2[sortedPlayers[i][2]] = sortedPlayers[i]#.append(i+1)
        self.sortedPlayers = sortedPlayers
        print(self.players2)

    def getPlayerRank_10(self, playerName, month):
        # 系统提供玩家名次查询接口，玩家能够查询自己名次前后10位玩家的分数和名次
        # month = datetime.now().month
        # key = 'players_%s' % month
        # player_rank = self.rdb.zrevrank(key, playerName)
        player_rank = self.players2[playerName][3]
        t = 10
        start = player_rank - t - 1
        if start < 0:
            start = 0
        end = player_rank + t
        return self.sortedPlayers[start:end]
# 测试代码

ranking = ActivityRanking()
ranking.addPlayer("Alice", 500)
ranking.addPlayer("Bob", 300)
ranking.addPlayer("Charlie", 400)
ranking.addPlayer("Dave", 200)
ranking.addPlayer("Dave", 200)

ranking.addPlayer("Dave1", 734)
ranking.addPlayer("Dave2", 2200)
ranking.addPlayer("Dave3", 1200)
ranking.addPlayer("Dave4", 2200)
ranking.addPlayer("Dave5", 3200)
# ranking.addPlayer("Charlie", 400)
ranking.addPlayer_40w()
ranking.calculateMonthlyRanking()

print(ranking.getPlayerRank_10("Dave3", 9))

# 40w
# 每月
# github
# 0-10000
# 多位一样，按照获取顺序 ok
