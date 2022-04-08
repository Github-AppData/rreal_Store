i, k = 0, 0

ko = 1
# # 11줄의 별 다이아몬드 2개 씩
# for i in range(0, 5):
#     print("&" * (5 - i), "*" * ko)
#     ko += 2

for k in range(0, 6):
    print("&" * k, "*" * (11 - (k * 2)))


    

