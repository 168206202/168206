'''graph'''

graph = {}
graph["music score"] = {}

graph["music score"]["disc"] = 5

graph["music score"]["poster"] = 0

graph["disc"] = {}

graph["disc"]["guitar"] = 15

graph["disc"]["drum"] = 20

graph["poster"] = {}

graph["poster"]["guitar"] = 30

graph["poster"]["drum"] = 35

graph["guitar"] = {}

graph["guitar"]["piano"] = 20

graph["drum"] = {}

graph["drum"]["piano"] = 10

graph["piano"] = {}


"""costs"""

infinity = float("inf")#定义infinity为无穷'''
costs = {}

costs["disc"] = 5

costs["poster"] = 0

costs["guitar"] = infinity

costs["drum"] = infinity

costs["piano"] = infinity


"""parents"""

parents = {}

parents['disc'] = 'yuepu'
 
parents['poster'] = 'yuepu'

parents['guitar'] = None 

parents['drum'] = None

parents['piano'] = None  


processed = []

lists = []

def find_lowest_cost_node(costs):
	
lowest_cost = float("inf")
	
lowest_cost_node = None
	
for node in costs:
		
cost = costs[node]
		
if cost < lowest_cost and node not in processed:
	
		lowest_cost = cost
			
lowest_cost_node = node
	
return lowest_cost_node

node = find_lowest_cost_node(costs)

while node is not None:
	
cost = costs[node]
	
neighbors =graph[node]
	
for n in neighbors.keys():
		
new_cost = cost + neighbors[n]
		
if costs[n] > new_cost:
			
costs[n] = new_cost
			
parents[n] =node
	
processed.append(node)
	
node = find_lowest_cost_node(costs)

for n,m in costs.items():
	
print(n + " : " + str(m))

print("\n\n")


""".............................................................."""

print("换钢琴最好路经：")
m = "piano"
while 1:
	
if m is "yuepu":
		
break
	
else:
		
lists.append(parents[m] + " -> ") 
		
m = parents[m]
while len(lists):
	l = lists.pop()
	
print(l)
print("piano ")

"""................................................................"""

