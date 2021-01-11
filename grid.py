import math
from enum import Enum, unique , auto

class  NeighboringNodes:
    grid=[]
    def __init__(self,size,debug): # Instantiate a size*size grid
        self._debug=debug
        self._size=size

        for row in range(self._size):
            for col in range(self._size):
                self.grid.append((row, col))

        if(self._debug):            # Accept debug as a parameter , If it is true displays the grid coordinates along with the index
            i=0
            for index, (x,y) in enumerate(self.grid):
                if(i<self._size):
                    print((x,y,index),end=" ")
                    i=i+1
                else:
                    i=0
                    print()
                    print((x,y,index),end=" ")
                    i=i+1
            print()
            
    def index_node(self,index):     # Accepts index of a node as its parameter and returns the (x,y) coordinate of that node.
        return self.grid[index]

    def topological_nodes(self,*args,type):     # Accepts either (x,y) or index , m(neighborhood radius), type(neighborhood type) and displays coordinates of all the neighboring nodes, based on the provided topological neighborhood type, within distance m.
        params=list(())
        self._x=args[0]
        self._y=args[1]
        self._m=args[2]
        self._type=type
        if(type==NeighborhoodType.SQUARE):
            for i in range(self._m, -self._m-1, -1):
                for j in range(self._m, -self._m-1, -1):
                    params.append((self._x-i,self._y-j))
                    print((self._x-i,self._y-j),end=" ")
                print()
            return params
        elif(type==NeighborhoodType.CROSS):
            for i in range(self._m, -self._m-1, -1): 
                if(i!=0):
                    for j in range(6*self._m):
                        print(end=" ")
                else:
                    for a in range(self._m, -self._m-1, -1):
                        params.append((self._x,self._y-a))
                        print((self._x,self._y-a),end="")
                        continue
                if((self._x-i,self._y)!=(self._x,self._y)):
                    params.append((self._x-i,self._y))
                    print((self._x-i,self._y))
                else:
                    print()
            return params 
        else:
            diamond_params=list(())
            self._m=self._m+1
            for i in range (0, self._m):
                params=[]
                c=self._m-i-1
                for j in range(6*(self._m-i-1)):
                    print(' ', end="")
                for a in range(-i, i+1):
                    params.append((self._x-c,self._y+a))
                    diamond_params.append((self._x-c,self._y+a))
                for b in params:
                    print(b,end="")
                print()
            for l in range (1,self._m):
                params=[]
                d=self._m-l-1
                for j in range(6*l):
                    print(' ', end="")
                for m in range (-d,d+1):
                    params.append((self._x+l, self._y+m))
                    diamond_params.append((self._x+l, self._y+m))
                for n in params:
                    print(n, end="")
                print()
            return diamond_params
@unique           
class NeighborhoodType(Enum):
    SQUARE = auto()
    CROSS = auto()
    DIAMOND = auto()


def main():
    params=[]
    edges=[]
    coordinates=list(())
    n=0
    crdnts=tuple(())
    flag=True
    #debug=True
    while flag:
        try:
            n=int(input("Enter the size of the matrix:? ")) # Accepts the user input for size of the matrix
            while True:
                if(n>0):
                    display=input("Please let us know if we want to display node corordinates? either True or False: ") # Accepts the user input either true of False for debug parameter
                    if display.lower()=="true":
                        debug=True
                    elif display.lower()=="false":
                        debug=False
                    else:
                        print("You have entered invalid input, your input should be either true or false")
                        continue 
                    nn=NeighboringNodes(n,debug)
                    flag=False
                    break
                else:
                    print("Enter any number greater than 0")
                    break
                
        except ValueError:   
            print("You have entered invalid input, Enter any number greater than zero.")
            flag=True
            continue    
    while True:
        try:
            index=(int(input("Enter the index number?"))) # Accepts the user input for Index number
            if(0<=index<n*n):
                node_coordinates=nn.index_node(index)
                print(node_coordinates)
                break
            else:
                print(f" You have given invalid input, Please enter the index in the range of 0-{n*n-1} ")
                continue 
        except IndexError:
            print(f"You have entered invalid input, Enter any number between 0-{n*n-1}.")
            continue
        except ValueError:
            print("You have entered invalid input, Enter any number greater than or eaqual to zero.")
            continue
    flag=True    
    while flag:
        try:
            option=int(input("Please enter either X & Y coordinates or node index, press 1 for coordinates and 2 for index ")) # Accepts the user input either X and Y coordinates or Index
            if (option==1):
                while True:
                    try:
                        X_crdnt=int(input("Please enter X coordinate "))
                    except ValueError:
                        print("Enter the integer value")
                        continue
                    if 0<=X_crdnt<=n-1:
                        flag=False
                        break
                    else:
                        print(f'Please enter the value between 0 and {n-1}')
                        continue
                while True:        
                    try:
                        Y_crdnt=int(input("Please enter Y coordinate "))
                    except ValueError:
                        print("Enter the integer value")
                        continue
                    if 0<=Y_crdnt<=n-1:
                        flag=False
                        break
                    else:
                        print(f'Please enter the value between 0 and {n-1}')
                        continue
                    
                crdnts=(X_crdnt,Y_crdnt)
                params.append(X_crdnt)
                params.append(Y_crdnt)
                    
            elif(option==2):
                flag=True
                while flag:
                    try:
                        index=int(input("Please enter index "))
                        flag=False
                    except ValueError:   
                        print("You have entered invalid input, Please provide input in requested format")
                        continue
                    if(0<=index<n*n):
                        node_crdnts=nn.index_node(index)
                        X_crdnt=node_crdnts[0]
                        Y_crdnt=node_crdnts[1]
                        crdnts=(X_crdnt,Y_crdnt)
                        print(crdnts)
                        params.append(X_crdnt)
                        params.append(Y_crdnt)
                        flag=False
                        break
                    else:
                        print(f" You have given invalid input, Please enter the index in the range of 0-{n*n-1} ")
                        flag=True
                        continue
                    
            else:
                print("You have entered invalid input, Please enter either 1 or 2")
                continue     
        except ValueError:   
            print("You have entered invalid input, Please provide input in requested format")
            continue
        break
    flag=True
    while flag:
        try:
            m=int(input(f"Enter the range of m between 0 and {int(n/2)} including {int(n/2)}: ")) # Accepts the user input for m: neighborhood radius
            if m in range(int((n/2)+1)):
                edges=[(X_crdnt,0),(X_crdnt,n-1),(0,Y_crdnt),(n-1,Y_crdnt)]
                for i in edges:
                    if int(math.dist(crdnts,i))>=m:
                        flag=False
                        validation=True

                    else:
                        print(f" The distance from the specified node to one or more edges of the grid is < {m}")  
                        flag=True
                        validation=False
                        break
                if validation:
                    break    
            else:
                continue
                            
        except ValueError:
            print("Please enter only integer value between the given range")
            flag=True
            continue
        
    while True:
        params.append(m)
        try:
            num=int(input("Enter the neighborhood type? 1 for SQUARE,2 for CROSS,3 for DIAMOND ")) # Accepts the user input for type: neighborhood type
            if num in range(4):
                type=NeighborhoodType(num)
                nds=nn.topological_nodes(*params,type=NeighborhoodType(num))
                print(nds)
                break
            else:
                print(f"Enter the numbers in the range from 1 to 3")
                continue
        except ValueError:
            print("You have entered invalid input,Please enter integer value between 1 and {}".format(len(NeighborhoodType)))
        
if __name__=="__main__":main()

 