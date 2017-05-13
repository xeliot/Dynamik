#sink
#shiny
#find the distance between sink and shiny

def translate(str1, str2):
    matrix = []
    for i in range(0, len(str1)):
        tmp = []
        for j in range(0, len(str2)):
            tmp.append(None)
        matrix.append(tmp)
    
    if str1[0] == str2[0]:
        matrix[0][0] = 0
    else:
        matrix[0][0] = 1
    
    for i in range(1, len(str2)):
        matrix[0][i] = matrix[0][i-1] + 1
    
    for i in range(1, len(str1)):
        matrix[i][0] = matrix[i-1][0] + 1

    print matrix

str1 = "sink"
str2 = "shiny"
print(translate(str1, str2))