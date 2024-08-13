#DFS
# Size of the grid
row, col = len(grid), len(grid[0])

def dfs(r, c, visit):
    # This code checks if a cell left, right, up or down of the current cell is a part of an "island" and does that until it maps the whole "island"
    if (r < 0 or c < 0 or r == row or c == col or grid[r][c] == '0' or (r, c) in visit):
        return
    visit.add((r, c))
    neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
    for nr, nc in neighbors:
        dfs(nr, nc, visit)

# Hashset for visited cells
visit = set()
res = 0
# Go through every cell, skip it if it is already part of an "island" the code has been through
for r in range(row):
    for c in range(col):
        if grid[r][c] == '1' and (r, c) not in visit:
            # Starts mapping an island, if there are cells thet don't touch the current "island" it is considered as a new "island"
            dfs(r, c, visit)
            res += 1
return res


# DFS is an algorithm of recursion, if you wanted all combinations of numbers from this array:
nums = [1, 2, 3, 4]
# You would do something like this:
res = []
def dfs(cur):
    if len(cur) == len(nums):
        res.append(cur)
        return
    for n in nums:
        if n not in cur:
            cur.append(n)
            dfs(cur.copy())
            cur.pop()

dfs([])
return res
