from typing import List
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        source_color = image[sr][sc]
        rows = len(image)
        cols = len(image[0])

        if source_color != newColor:
            q = deque([(sr, sc)])
            while q:
                x, y = q.popleft()
                image[x][y] = newColor
                pair1 = [0, 0, 1, -1]
                pair2 = [1, -1, 0, 0]

                for i in range(4):
                    neighbour_x = x+pair1[i]
                    neighbour_y = y+pair2[i]
                    if neighbour_x >= 0 and neighbour_x < rows and neighbour_y >= 0 and neighbour_y < cols and image[neighbour_x][neighbour_y] == source_color:
                        q.append((neighbour_x, neighbour_y))
        return image

obj = Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
res = obj.floodFill(image, sr, sc, newColor)

for i in range(len(res)):
    for j in range(len(res[0])):
        print(res[i][j], end=" ")
    print()

