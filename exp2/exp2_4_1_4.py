#使用集合
play_basketball = ['a','b','c','d','e']
play_game = ['a','b','c','f','g']
both_play=[]
for name in play_basketball:
    if name in play_game:
        both_play.append(name)
print(both_play)