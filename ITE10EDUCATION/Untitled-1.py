def print_list(matrix):
    for row in matrix:
        print(row)

def test(list):
    d = [
            [list[0][0], list[0][1], list[0][2]],
            [list[1][0], list[1][1], list[1][2]],
            [list[2][0], list[2][1], list[2][2]]
            ]
    
    d1 = ((d[1][1])*(d[2][2]))
    d2 = ((d[1][2])*(d[2][1]))
    if d2 < 0:
        d2 = d2*(-1)
        d3 = (d1 + d2)*(d[0][0])
    else:
        d3 = (d1 - d2)*(d[0][0])
        
    m1 = [[d[1][1],d[1][2]],
               [d[2][1],d[2][2]]
              ]
                
    print_list(m1)
    print("{}(({} × {}) - ({} × {})) = {}".format(d[0][0], d[1][1], d[2][2], d[1][2], d[2][1], d3))
        
    d4 = ((d[1][0])*(d[2][2]))
    d5 = ((d[1][2])*(d[2][0]))
    if d5 < 0:
        d5 = d5*(-1)
        d6 = (d4 + d5)*(d[0][1])
    else:
        d6 = (d4 - d5)*(d[0][1])
    
    m2 = [[d[1][0],d[1][2]],
               [d[2][0],d[2][2]]
              ]
    print("\n")
    print_list(m2)
    print("{}(({} × {}) - ({} × {})) = {}".format(d[0][1], d[1][0], d[2][2], d[1][2], d[2][0], d6))
        
    d7 = ((d[1][0])*(d[2][1]))
    d8 = ((d[1][1])*(d[2][0]))
    if d8 < 0:
        d8 = d8*(-1)
        d9 = (d7 + d8)*(d[0][2])
    else:
        d9 = (d7 - d8)*(d[0][2])
    
    m3 = [[d[1][0],d[1][1]],
               [d[2][0],d[2][1]]
              ]
    print("\n")
    print_list(m3)        
    print("{}(({} × {}) - ({} × {})) = {}".format(d[0][2], d[1][0], d[2][1], d[1][1], d[2][0], d9))
    
    global ans
    ans = float(((d3 - (d6) + (d9))))
    
    print("\n({}) - ({}) + ({}) = {}".format(d3,d6,d9,ans))
    
    return ans
"""    
matrix_3x4 = [[0, 0, 0, 0] for _ in range(3)]
for i in range(3):
    for j in range(4):
        element = int(input(f"Enter value for element at position ({i}, {j}): "))
        matrix_3x4[i][j] = element
"""
matrix_3x4 = [
        [2, 5, 2,-38],
        [3, -2, 4, 17],
        [-6, 1, -7, -12]
        ]
  
print("Original matrix = ")       
print_list(matrix_3x4)

g = [
    matrix_3x4[0][:3],
    matrix_3x4[1][:3],
    matrix_3x4[2][:3]
]

print("\n")
test(g)
print("\nD: {}".format(ans))
later = [float(ans)]

h = [[0, 0, 0] for _ in range(3)]
for i in range(3):
    h[i][0] = matrix_3x4[i][3]
    h[i][1] = matrix_3x4[i][1]
    h[i][2] = matrix_3x4[i][2]

print("\n\nFor Dx:\n")
print_list(h)
print("\n")  
test(h)
print("\nDx: {}".format(ans))
later.append(ans)

j = [[0, 0, 0] for _ in range(3)]
for i in range(3):
    j[i][0] = matrix_3x4[i][0]
    j[i][1] = matrix_3x4[i][3]
    j[i][2] = matrix_3x4[i][2]

print("\n\nFor Dy:\n")
print_list(j)
print("\n")  
test(j)
print("\nDy: {}".format(ans))
later.append(ans)

k = [[0, 0, 0] for _ in range(3)]
for i in range(3):
    k[i][0] = matrix_3x4[i][0]
    k[i][1] = matrix_3x4[i][1]
    k[i][2] = matrix_3x4[i][3]

print("\n\nFor Dz:\n")
print_list(k)
print("\n")  
test(k)
print("\nDz: {}".format(ans))
later.append(ans)

ansx = float(later[1]/later[0])
ansy = later[2]/later[0]
ansz = later[3]/later[0]

print(f"\nX: {later[1]}/{later[0]} = {ansx}")
print(f"Y: {later[2]}/{later[0]} = {ansy}")
print(f"Z: {later[3]}/{later[0]} = {ansz}")