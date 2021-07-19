from itertools import permutations as per

def solution(user_id, banned_id):
    per_user = list(per(user_id, len(banned_id)))
    banned = []
    for user in per_user:
        if isMatch(user, banned_id):
            user = set(user)
            if user not in banned:
                banned.append(user)
    return len(banned)

def isMatch(user_set, banned_set):
    for i in range(len(user_set)):
        if len(user_set[i]) != len(banned_set[i]):
            return False
        for j in range(len(user_set[i])):
            if banned_set[i][j] == '*':
                pass
            elif user_set[i][j] != banned_set[i][j]:
                return False
    return True




print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
