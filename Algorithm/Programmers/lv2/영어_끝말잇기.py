def solution(n, words):
    answer = [0,0]
    spoken = []
    for i in range(len(words)):
        if i>0 and (words[i][0] != words[i-1][-1] or words[i] in spoken):
            return [(i%n)+1, (i//n)+1]
        spoken.append(words[i])
    return answer


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))