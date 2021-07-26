v = lambda m: all(len(m[0]) == len(x) for x in m[1:])

def f(a, b):
    r = []

    for i in range(2):
        if not v([a, b][i]):
            raise ValueError('Matriz #%d não é válida.' % i)
    
    if len(a[0]) != len(b):
        raise ValueError('Não é possível obter o produto.')
    
    for x in a:
        tm = []
        for i, n in enumerate(b[0]):
            y = 0
            for ix, nx in enumerate(x):
                # Somar valores booleanos é uma operação OR (Pega o maior valor)
                # Multiplicar valores booleanos é uma operação AND (Pega o menor valor)
                '''
                    Soma | OR            Mult | AND
                    1 0 -> O maior é 1   1 0 -> O menor é 0
                    1 1 -> O maior é 1   0 1 -> O menor é 0
                    0 1 -> O maior é 1   0 0 -> O menor é 0
                    0 0 -> O maior é 0   1 1 -> O menor é 1
                '''
                y |= nx & b[ix][i]
            tm.append(y)
        r.append(tm)
    
    return r

print(f([[1, 1, 0], [0, 1, 0], [0, 0, 1]], [[1, 0, 0], [1, 1, 1], [0, 0, 1]]))