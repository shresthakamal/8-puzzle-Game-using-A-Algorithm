import numpy as np

class PriorityQueue(object):
	def __init__(self):
		self.queue = []
		self.goal_state = np.array([
			1,2,3,
			8,0,4,
			7,6,5
		])

	def h(self,start,goal):
				""" Calculates the different between the given puzzles """
				start = np.array(start).reshape((3,3))
				goal = np.array(goal).reshape((3,3))

				temp = 0
				for i in range(0,3):
					for j in range(0,3):
						if start[i][j] != goal[i][j] and start[i][j] != 0:
							temp += 1
				return temp

	def __str__(self):
		return ' '.join([str(i) for i in self.queue])

# for checking if the queue is empty
	def isEmpty(self):
		return len(self.queue) == []

# for inserting an element in the queue
	def push(self,sentState,checkValue=True,value=0):
		if checkValue:
			manHattenDistance = self.h(sentState.state,self.goal_state)
			self.queue.append([manHattenDistance,sentState])
		else:
			self.queue.append(value)

# for popping an element based on Priority
	def pop(self,value=True):
		try:
			min = 0
			for i in range(len(self.queue)):
				if value:
					if self.queue[i][0] < self.queue[min][0]:
						min = i
				else:
					if self.queue[i] < self.queue[min]:
						min = i
			item = self.queue[min]
			del self.queue[min]
			return item
		except IndexError:
			print()
			exit()

q = PriorityQueue()
q.push([1,0,0,1],False,10)
q.push([1,0,0,1],False,40)
q.push([1,0,0,1],False,30)
q.push([1,0,0,1],False,20)
print(q.pop(False))
print(q.pop(False))
print(q.pop(False))
print(q.pop(False))


