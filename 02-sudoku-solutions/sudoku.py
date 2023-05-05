solve = [[[5,3,0],[6,0,0],[0,9,8]],[[0,7,0],[1,9,5],[0,0,0]],[[0,0,0],[0,0,0],[0,6,0]],[[8,0,0],[4,0,0],[7,0,0]],[[0,6,0],[8,0,3],[0,2,0]],[[0,0,3],[0,0,1],[0,0,6]],[[0,6,0],[0,0,0],[0,0,0]],[[0,0,0],[4,1,9],[0,8,0]],[[2,8,0],[0,0,5],[0,7,9]]]
#solves= [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

def searchs(grid, block, block_index, val):
    x0 = block_index//3*3
    if block_index // 3 >1:
        y0 = block_index- 6
    elif block_index//3 >0:
        y0 = block_index -3
    else:
        y0 = block_index
    

    if block == 1 or block == 4 or block == 7:
        for x in range(0,3):
            if grid[block+1][x0+x] == val or grid[block+2][x0+x] == val:
                return False
    elif block == 2 or block == 5 or block == 8:
        for x in range(0,3):
            if grid[block-1][x0+x] == val or grid[block+1][x0+x] == val:
                return False
    else:
            for x in range(0,3):
                if grid[block-1][x0+x] == val or grid[block-2][x0+x] == val:
                    return False
    
    if block == 1 or block == 2 or block == 3:
        for x in range(0,9,3):
            if grid[block+3][y0+x] == val or grid[block+6][y0+x] == val:
                return False
    elif block == 4 or block == 5 or block == 6:
        for x in range(0,9,3):
            if grid[block-3][y0+x] == val or grid[block+3][y0+x] == val:
                return False
    else:
        for x in range(0,9,3):
            if grid[block-3][y0+x] == val or grid[block-6][y0+x] == val:
                return False      

    if val in grid[block]:
        return False

    return True 
    
        
    
def solve_sedoku(grid):
    # sorting info into desiarble format.
    # change a few steps to sort different data inputs
    grids = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
    for count, point_block in enumerate(grid, start=1):
        for point_rows in point_block:
            for point in point_rows:
                grids[count].append(point)
    check_grid = 0
    check_grid_cont =  True
    print(grids)
    while check_grid_cont : 

        for block, group_points in grids.items():
            checks = {}
            check = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
            print(group_points)
            for count, point in enumerate(group_points, start=0):
                temp = []
                block_index = 0
                if point == 0:
                    
                    block_index = count
                    print(block_index)
                    for i in range(1,10):
                        if searchs(grids, block, block_index,i):
                            temp.append(i)
                    checks[block_index] = temp
                    for x in temp:
                        check[x] += 1
            print(checks)
            print(check)
            for number ,number_count in check.items():
                if number_count == 1:
                    for ind,possibilities in checks.items():
                        if number in possibilities:
                            check_grid = 0
                            grids[block][ind]= number
                            print ("changed")
                            print(check_grid_cont)
        check_grid += 1
        if check_grid > 1:
            for gridss in grids.values():
                if 0 in gridss:
                    return "invalid" 
            check_grid_cont = False
    
    return grids

print(solve_sedoku(solve))
        
        
