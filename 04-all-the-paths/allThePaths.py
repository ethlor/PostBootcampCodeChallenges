# if all the boxes have been seen end
def all_paths(maze,current=(0,0), path=[]):
    paths = []
 
    for countt, top_bottom in enumerate(maze, start =0):
        for countr, room in enumerate(top_bottom,start = 0):
            cord_check = (countr,countt)
        
            if cord_check == current:
                               
                if 1 in maze[countt][countr]: # if a room has no open doors end the path

                    for countd, door in enumerate(room,start=0):
                        
                        if door == 1:
                            cord_check = (countr,countt)
                            path.append(cord_check)
                            

                            # rules for determining the next room to look at
                            if countd == 0 and countt != 0:
                                cord_check = (countr,countt-1)
                            elif countd == 1 :
                                if countr!= (len(maze[countt])-1):
                                    cord_check = (countr+1,countt)
                                else:
                                    cord_check = (0,countt)  
                            elif countd == 2 :
                                if countt == len(maze)-1:
                                    cord_check = (countr,0)
                                else:
                                    cord_check = (countr,countt+1)   
                            elif countd == 3:
                                cord_check = (countr-1,countt)

                            # edits to the door if its been passed through and then correcting it when you return for the loop    
                            maze[countt][countr][countd]=0
                            all_paths(maze,cord_check,path)
                            maze[countt][countr][countd]=1
                            

                            paths.append(path)

                            path = []
# if the door leads back to a room you need to continue a loop that was previously looked at
# if you went throug a door you close it               
   
    return paths
                        

                        


            
    
maze = [[[0,1,1,0],[0,0,0,1]],[[0,0,1,0]]]
print(all_paths(maze))



