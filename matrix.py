def only_complex(a,b):
    res = []
    mat = [a,b]
    for j in range(2):
        res += [mat[j][i] for i in range(len(a)) if type(complex()) == type(mat[j][i])]
        # for i in range(len(a)):
        #     if type(complex()) == mat[j][i]:
        #         res.append(mat[j][i])
    return tuple(res)
