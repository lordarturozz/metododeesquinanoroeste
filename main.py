matriz = []
matriz2 = []

filas = int(input('Ingrese el número de filas: ')) + 1
columnas = int(input('Ingrese el número de columnas: ')) + 1

for i in range(filas):
    matriz.append([0] * columnas)
    matriz2.append([0] * columnas)

print('Ingrese ofertas y demandas')
while True:
    sumaF, sumaC = 0, 0
    for f in range(filas - 1):
        matriz[f][columnas - 1] = int(input('Ingrese oferta [%d]: ' % (f + 1)))
        matriz2[f][columnas - 1] = matriz[f][columnas - 1]
        sumaF += matriz[f][columnas - 1]
    for c in range(columnas - 1):
        matriz[filas - 1][c] = int(input('Ingrese demanda [%d]: ' % (c + 1)))
        matriz2[filas - 1][c] = matriz[filas - 1][c]
        sumaC += matriz[filas - 1][c]
    if sumaF == sumaC:
        break
    else:
        print('Las sumas de las ofertas y demandas no coinciden. Intente nuevamente.')

print('Ingrese Inventario/Stock/Almacen.')
for f in range(filas - 1):
    for c in range(columnas - 1):
        matriz[f][c] = int(input('Ingrese elemento [%d][%d]: ' % (f, c)))

print('Calcular movimientos -> Matriz2')
posF, posC = 0, 0
while True:
    sumaF, sumaC = 0, 0
    for f in range(filas - 1):
        sumaF += matriz2[f][posC]
    for c in range(columnas - 1):
        sumaC += matriz2[posF][c]

    vo = matriz[filas - 1][posC] - sumaF
    vi = matriz[posF][columnas - 1] - sumaC

    if vo < vi:
        menor = vo
        matriz2[posF][posC] = menor
        posC += 1
    elif vi < vo:
        menor = vi
        matriz2[posF][posC] = menor
        posF += 1
    else:
        menor = vo
        matriz2[posF][posC] = menor
        posF += 1
        posC += 1

    if posF == filas - 1 or posC == columnas - 1:
        break

print('Matriz1 -> Inventario')
for p in range(filas):
    print(matriz[p])

print('Matriz -> Movimientos')
for p in range(filas):
    print(matriz2[p])