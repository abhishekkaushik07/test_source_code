#solving sudoku

def is_arr_fill(a):
    flag=1
    for i in range(0,9):
        for j in range(0,9):
            if(a[i][j]==0):
                flag=0
                return i,j
                break

    if(flag==1):
        return 1

def is_safe(a,row_posi,column_posi,num):
    flag=1
    for i in range(9):
        if(num == a[i][column_posi]):
            flag=0
    for j in range(9):
        if(num == a[row_posi][j]):
            flag=0

    for i in range(3):
        for j in range(3):
            if(a[(row_posi- row_posi%3) + i][(column_posi- column_posi%3) + j] == num):
                flag=0

    if(flag==1):
        return True
    else:
        return False

def print_ans(a):
    for i in range(9):
        for j in range(9):
            print(a[i][j],end = " ")
        print()


def solve_it(a):
    if(is_arr_fill(a) == 1):
        return 1
    else:
        x,y = is_arr_fill(a)

    for num in range(1,10):
        if( is_safe(a,x,y,num) ):
            a[x][y] = num

            if( solve_it(a) == 1 ):
                return 1
            
            a[x][y]=0

    return 0







#main program
if __name__=="__main__":
    n=int(input())
    while(n>0):
        m=9
        a = [[int(j) for j in input().split()] for i in range(m)]
        

        if( solve_it(a) == 1 ):
            print_ans(a)
        else:
            print("does not exist")

        n=n-1
    
    

    




