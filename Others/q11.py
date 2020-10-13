'''
2D Spiral Array

'''


def spiral(n):
    nopoints = 0
    spir_arr = [[0 for i in range(n)] for j in range(n)]

    col = 0
    row = 0
    pt_seen = []
    while (row,col) not in pt_seen:
        while col < n and (row,col) not in pt_seen:
            nopoints += 1
            spir_arr[row][col] = nopoints


            pt_seen.append((row,col))
            col += 1

        col -= 1
        row+=1
        while row < n and (row,col) not in pt_seen:
            nopoints += 1
            spir_arr[row][col] = nopoints
            pt_seen.append((row,col))
            row+=1

        row -=1
        col-=1

        while col >=0 and (row, col) not in pt_seen:
            nopoints += 1
            spir_arr[row][col] = nopoints

            pt_seen.append((row, col))
            col -= 1



        row-=1
        col+=1
        while row >=0 and (row,col) not in pt_seen:
            nopoints += 1
            spir_arr[row][col] = nopoints

            pt_seen.append((row,col))
            row -= 1


        col+=1
        row+=1



    return spir_arr


print(spiral(4))




