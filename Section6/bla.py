stages = [2, 1, 2, 6, 2, 4, 3, 3]
user_status = {}
users = len(stages)
for stage in range(1, 5 + 1):
    if users == 0:
        user_status[stage] = 0
        continue
    count = stages.count(stage)
    user_status[stage] = count / users
    users -= count
print(user_status)
print (sorted(user_status, key=lambda x: user_status[x], reverse=True))