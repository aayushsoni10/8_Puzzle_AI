import sys
import heapq
from random import randint

# This class is used to Create the n X n puzzle

class EightPuzzle:

    # Initiating the object
	def __init__(self,size):
		self.size=size
		self.puzzle=[]
		self.zero=(0,0)
		self.moves=["U","D","L","R"]
		count=1
		for i in range(0,size):
			self.puzzle.append([])
			for j in range(0,size):
				self.puzzle[i].append(count)
				count+=1
		self.puzzle[size-1][size-1]=0
		self.zero=(size-1,size-1)

    #Converting our puzzle in string
	def readPuzzle(self,string):
		a=string.split(" ")
		count=0
		for i in range(0,self.size):
			for j in range(0,self.size):
				if int(a[count])==0:
					self.zero=(i,j)
				self.puzzle[i][j]=int(a[count])
				count+=1

    #Checking if the puzzle is correct
	def checkPuzzle(self):
		count=1
		for i in range(0,self.size):
			for j in range(0,self.size):
				if self.puzzle[i][j]!=(count%(self.size*self.size)):
					return False
				count+=1
		return True

	#Swapping 2 elemets in the matrix
	def swap(self,(x1,y1),(x2,y2)):
		temp=self.puzzle[x1][y1]
		self.puzzle[x1][y1]=self.puzzle[x2][y2]
		self.puzzle[x2][y2]=temp

    #move functions
	def up(self):
		if (self.zero[0]!=0):
			self.swap((self.zero[0]-1,self.zero[1]),self.zero)
			self.zero=(self.zero[0]-1,self.zero[1])
	def down(self):
		if (self.zero[0]!=self.size-1):
			self.swap((self.zero[0]+1,self.zero[1]),self.zero)
			self.zero=(self.zero[0]+1,self.zero[1])

	def left(self):
		if (self.zero[1]!=0):
			self.swap((self.zero[0],self.zero[1]-1),self.zero)
			self.zero=(self.zero[0],self.zero[1]-1)


	def right(self):
		if (self.zero[1]!=self.size-1):
			self.swap((self.zero[0],self.zero[1]+1),self.zero)
			self.zero=(self.zero[0],self.zero[1]+1)

	#Printing the puzzle in matrix form
	def printPuzzle(self):
		for i in range(0,self.size):
			for j in range(0,self.size):
				print self.puzzle[i][j],
			print ""
			#print

    #Performing Move on the matrix
	def doMove(self,move):
		if move=="U":
			self.up()
		if move=="D":
			self.down()
		if move=="L":
			self.left()
		if move=="R":
			self.right()

	def permute(self,numPerm):
		for i in range(0,numPerm):
			self.doMove(self.moves[randint(0,3)])

	def parseMoveSequence(self,string):
		for m in string:
			self.doMove(m)


#Taking inputs from command line for the structure of the puzzle


#In our case the size is 3 X 3 ~= 8 PUZZLE

t1=EightPuzzle(3)
t1.permute(3)

#Printing the initial form of Puzzle
print("Initial puzzle")
t1.printPuzzle()
# Using heap for level ordered bfs for the puzzle with initial puzzle layer = 0
leaves = []
heapq.heappush(leaves, (0, t1.puzzle))
l = 0
# Variable TBF to store the total branching factor
TBF = 0
# Variable NS to store the total number of states
NS = 0
# I have checked the branching factor till level 13 only due to bad processor
# If we increase the level then we might get a more accurate result ~ 2.66
a = [0,0,0,0,0,0,0,0,0,0,0,0,0]
ind = 0
values = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
# Performing BFS
while leaves:
    t = [[0,0,0],[0,0,0],[0,0,0]]

    # Popping an element which has the least level
    next_item = heapq.heappop(leaves)

    # Variable r is storing the matrix
    r = next_item[1]

    # Variable l is storing the current puzzle/ matrix level number
    l = next_item[0]

    if(ind>11):
        break
    # Printing the TBF AND NS for different level constraints
    if l>(ind+1) and a[ind]==0:
        print " Results till level<=", ind+1
        print "     Total branching factor = ", TBF
        print "     Total number of states for the puzzle(n) = ", NS
        print "     Average branching factor(b) = ", ((TBF+0.0)/NS)
        a[ind]=1
        values[ind] = ((TBF+0.0)/NS)
        tm = 1
        for x in range(ind+2):
            tm = tm*values[ind]
        k = NS/tm
        print "     Applying the formula n = k(b)^(d+1), value of k = ", k
        ind = ind +1

    # Incrementing the number of states
    NS=NS+1

    # Storing the currently popped matrix (r) in variable t
    t[0][0] = r[0][0]
    t[0][1] = r[0][1]
    t[0][2] = r[0][2]
    t[1][0] = r[1][0]
    t[1][1] = r[1][1]
    t[1][2] = r[1][2]
    t[2][0] = r[2][0]
    t[2][1] = r[2][1]
    t[2][2] = r[2][2]
    '''IMPORTANT: TO print the current state we can print the matrix in variable t'''

    # Performing moves depending on the place where 0(or empty cell) is present
    # Then pushing the new matrix with l+1 i.e. current level + 1 in the heap
    if(r[0][0]==0):
        TBF = TBF+2
        temp = t[0][1]
        t[0][1] = 0
        t[0][0] = temp
        heapq.heappush(leaves, (l+1, t))
        temp = t[0][0]
        t[0][0] = 0
        t[0][1] = temp
        temp = t[1][0]
        t[1][0]=0
        t[0][0] = temp
        heapq.heappush(leaves, (l+1, t))
    elif(r[0][1]==0):
        TBF = TBF+3
        temp = t[1][1]
        t[1][1]=0
        t[0][1] = temp
        heapq.heappush(leaves, (l+1, t))
        temp = t[0][1]
        t[0][1] = 0
        t[1][1] = temp
        temp = t[0][2]
        t[0][2]=0
        t[0][1] = temp
        heapq.heappush(leaves, (l+1, t))
        temp = t[0][1]
        t[0][1] = 0
        t[0][2] = temp
        temp = t[0][0]
        t[0][0]=0
        t[0][1] = temp
        heapq.heappush(leaves, (l+1, t))
    elif(r[1][0]==0):
        TBF = TBF+3
        temp = t[1][1]
        t[1][1]=0
        t[1][0] = temp
        heapq.heappush(leaves, (l+1, t))
        temp = t[1][0]
        t[1][0] = 0
        t[1][1] = temp
        temp = t[2][0]
        t[2][0]=0
        t[1][0] = temp
        heapq.heappush(leaves, (l+1, t))
        temp = t[1][0]
        t[1][0] = 0
        t[2][0] = temp
        temp = t[0][0]
        t[0][0]=0
        t[1][0] = temp
        heapq.heappush(leaves, (l+1, t))
    elif(r[0][2]==0):
        TBF = TBF+2
        temp = t[0][1]
        t[0][1]=0
        t[0][2] = temp
        heapq.heappush(leaves, (l+1, t))
        temp = t[0][2]
        t[0][2] = 0
        t[0][1] = temp
        temp = t[1][2]
        t[1][2]=0
        t[0][2] = temp
        heapq.heappush(leaves, (l+1, t))
    elif(r[1][2]==0):
        TBF = TBF+3
        temp = t[1][1]
        t[1][1]=0
        t[1][2] = temp
        heapq.heappush(leaves, (l+1, t))
        temp = t[1][2]
        t[1][2] = 0
        t[1][1] = temp
        temp = t[0][2]
        t[0][2]=0
        t[1][2] = temp
        heapq.heappush(leaves, (l+1, t))
        temp = t[1][2]
        t[1][2] = 0
        t[0][2] = temp
        temp = t[2][2]
        t[2][2]=0
        t[1][2] = temp
        heapq.heappush(leaves, (l+1, t))
    elif(r[1][1]==0):
        TBF = TBF+4
        temp = t[0][1]
        t[0][1]=0
        t[1][1] = temp
        heapq.heappush(leaves, (l+1, t))
        temp = t[1][1]
        t[1][1] = 0
        t[0][1] = temp
        temp = t[1][2]
        t[1][2]=0
        t[1][1] = temp
        heapq.heappush(leaves, (l+1, t))
        temp = t[1][1]
        t[1][1] = 0
        t[1][2] = temp
        temp = t[1][0]
        t[1][0]=0
        t[1][1] = temp
        heapq.heappush(leaves, (l+1, t))
        temp = t[1][1]
        t[1][1] = 0
        t[1][0] = temp
        temp = t[2][1]
        t[2][1]=0
        t[1][1] = temp
        heapq.heappush(leaves, (l+1, t))
    elif(r[2][1]==0):
        TBF = TBF+3
        temp = t[1][1]
        t[1][1]=0
        t[2][1] = temp
        heapq.heappush(leaves, (l+1, t))
        temp = t[2][1]
        t[2][1] = 0
        t[1][1] = temp
        temp = t[2][2]
        t[2][2]=0
        t[2][1] = temp
        heapq.heappush(leaves, (l+1, t))
        temp = t[2][1]
        t[2][1] = 0
        t[2][2] = temp
        temp = t[2][0]
        t[2][0]=0
        t[2][1] = temp
        heapq.heappush(leaves, (l+1, t))
    elif(r[2][0]==0):
        TBF = TBF+2
        temp = t[1][0]
        t[1][0]=0
        t[2][0] = temp
        heapq.heappush(leaves, (l+1, t))
        temp = t[2][0]
        t[2][0] = 0
        t[1][0] = temp
        temp = t[2][1]
        t[2][1]=0
        t[2][0] = temp
        heapq.heappush(leaves, (l+1, t))
    elif(r[2][2]==0):
        TBF = TBF+2
        temp = t[2][1]
        t[2][1]=0
        t[2][2] = temp
        heapq.heappush(leaves, (l+1, t))
        temp = t[2][2]
        t[2][2] = 0
        t[2][1] = temp
        temp = t[1][2]
        t[1][2]=0
        t[2][2] = temp
        heapq.heappush(leaves, (l+1, t))

ABF = 0.0
for x in range(13):
    ABF = ABF + values[x]
ABF = (ABF/13)
print "Overall average branching factor = ", ABF
tm = 1
for x in range(ind+1):
    tm = tm*ABF
k = NS/tm
print "Applying the formula n = k(b)^(d+1), value of k = ", k
if(k>=0 and k<2):
    print "The value of k is in between 0 and 2, Hence Satisfied."
