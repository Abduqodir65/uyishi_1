# s = input(">>> ")
# lst = []
# st = ""
# for i in s:
#     if i not in st:
#         st = st + i
#     else:
#         lst.append(st)
#         st = i
# lst.append(st)
# max = max(lst, key=lambda x: len(x))
# print(max)

# suz = input("nimadir yozing: ")
# i = len(suz) // 2
# suz = suz[-i:] + suz[:-i]
# print(suz)

# suz = input(">>> ")
# for i in suz.split():
#     quti = 1
#     m = ""
#     for j in i:
#         if j in m:
#             quti = 0
#             break
#         if j.isalpha():
#             m += j
#     if quti:
#         n = len(m) // 2
#         m = m[-n:] + m[:-n]
#         print(m)