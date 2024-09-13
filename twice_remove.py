def remove_twice(s: str) -> str:
    vowels = "ёуеыаоэяию"
    i = 0
    res = ""
    while i < len(s):
        if s[i] in vowels:
            if i+1==len(s):break
            while s[i]==s[i+1]:
                i+=1
                if i+1==len(s):break
        res+=s[i]
        i+=1
    return res

# def remove_twice(s: str) -> str:
#     vowels = "ёуеыаоэяию"
#     i = 0
#     res = ""
#     while i < len(s):
#         if s[i] in vowels:
#             j = i
#             try:
#                 while s[j]==s[j+1]:
#                     j+=1
#             except Exception:
#                 i=j
#             i=j
#         res+=s[i]
#         i+=1
#     return res
