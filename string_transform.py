#sink
#shiny
#PROBLEM 1
#find the distance between sink and shiny

def print_matrix(matrix):
    for ar in matrix:
        print ar

def translate(str1, str2):

    #INITIALIZE MATRIX ACCORDING TO STRING 1 and STRING 2 LENGTH
    matrix = []
    for i in range(0, len(str1)):
        tmp = []
        for j in range(0, len(str2)):
            tmp.append(None)
        matrix.append(tmp)
    #INITALIZE FIRST ROW AND FIRST COLUMN
    if str1[0] == str2[0]:
        matrix[0][0] = 0
    else:
        matrix[0][0] = 1
    for i in range(1, len(str2)):
        matrix[0][i] = matrix[0][i-1] + 1
    for i in range(1, len(str1)):
        matrix[i][0] = matrix[i-1][0] + 1
    #FILL IN THE BOARD
    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            possible = []
            if str1[i] == str2[j]:
                possible.append(matrix[i-1][j-1])
            else:
                possible.append(matrix[i-1][j-1]+1)
            possible.append(matrix[i][j-1]+1)
            possible.append(matrix[i-1][j]+1)
            matrix[i][j]=min(possible)

    #print matrix to make sure everything is ok
    print_matrix(matrix)

    #return the bottom left element of the matrix
    return matrix[len(str1)-1][len(str2)-1]

#str1 = "sink"
#str2 = "shiny"

str1 = "abcd"
str2 = "bcfg"
distance = translate(str1, str2)
print distance