# def solution(routes):
#     routes.sort(key=lambda x: x[1])
#     leng = len(routes)
#     ch = [0] * leng
#     res = 0
#
#     for i in range(leng):
#         if ch[i] == 0:
#             camera = routes[i][1]
#             res += 1
#         for j in range(i+1, leng):
#             if routes[j][0] <= camera <= routes[j][1]:
#                 ch[j] = 1
#     return res

def solution(routes):
    routes.sort(key=lambda x:x[1])
    camera = -30001
    answer = 0

    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer





print(solution(	[[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))
