def remove_twice(s: str):
    dict_char = {"у":0,"е":0,"ы":0,"а":0,"о":0,"я":0,"и":0,"ю":0,"ё":0, "э":0,}
    res = ""
    for i in s:
        try:
            if dict_char[i]==1:
                continue
            dict_char[i]+=1
            res += i
        except:
            res += i
    return res