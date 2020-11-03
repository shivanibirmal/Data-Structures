##### using DFS gives maximum recursion depth reached ######

visited = 'x'
def isValid(i,j,picture,curr_char):
    rows = len(picture)
    col = len(picture[0])
    if (i< 0 or j < 0 or i >= rows or j >= col or picture[i][j]!=curr_char):
        return False
    else:
        return True

def dfs(row,col, picture, curr_char):

    picture[row][col] = 'x'
    pair1 = [0,1,-1,0]
    pair2 = [1,0,0,-1]

    for i in range (len(pair1)):
        if isValid(row+pair1[i], col+pair2[i], picture,curr_char):
            dfs(row+pair1[i], col+pair2[i],picture,curr_char)

def strokesRequired(picture):
    count = 0
    for i in picture:
        picture[i] = list(picture)

    for i in range(0, len(picture)):
        for j in range(0,  len(picture[0])):
            if picture[i][j] != visited:
                count += 1
                dfs(i,j, picture,picture[i][j])
    return count

picture = ["aabba", "aabba", "aaacb"]
min_strokes = strokesRequired(picture)





