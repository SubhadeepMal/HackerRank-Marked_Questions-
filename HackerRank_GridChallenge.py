
def check(grid):
    a=0
    for x in range(len(grid[0])):        
        for y in range(len(grid)-1):
            if str(grid[y][x])<=str(grid[y+1][x]):
                a+=1
            else:
                return 'NO'
    if a==(len(grid[0])*(len(grid)-1)):
        return 'YES'
        
        
        
def gridChallenge(grid):
    newgrid=[]
    for x in range(len(grid)):
        s="".join(sorted(grid[x])) 

        # The above helps us to sort an string , 
        # since .append() fn is not valid for strings.
        
        newgrid.append(s)
    
    return check(newgrid)
    
t = int(input().strip())

for t_itr in range(t):
    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = gridChallenge(grid)
    print(result)
