import random
import math

gride_size = 25
populationlen = 6
genloop = 15
mutation_rate = 0.1
alpha = 1000  
beta = 2      
gamma = 1     


components = {
    "ALU": (5, 5),
    "Cache": (7, 4),
    "Control": (4, 4),
    "Register": (6, 6),
    "Decoder": (5, 3),
    "Floating": (5, 5)
}

component_name = list(components.keys())
connetion = [
    ("Register", "ALU"),
    ("Control", "ALU"),
    ("ALU", "Cache"),
    ("Register", "Floating"),
    ("Cache", "Decoder"),
    ("Decoder", "Floating")
]
def center(x, y, w, h):
    return (x + w / 2, y + h / 2)

def euclidean(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def bounding_box(chromosome):
    xs = [x for x, y in chromosome.values()]
    ys = [y for x, y in chromosome.values()]
    x_max = max(x + components[name][0] for name, (x, y) in chromosome.items())
    y_max = max(y + components[name][1] for name, (x, y) in chromosome.items())
    x_min = min(xs)
    y_min = min(ys)
    return (x_max - x_min) * (y_max - y_min)

def has_overlap(a, b):
    (x1, y1), (x2, y2) = a[1], b[1]
    w1, h1 = components[a[0]]
    w2, h2 = components[b[0]]
    A_left = x1
    A_right = x1 + w1
    A_bottom = y1
    A_top = y1 + h1
    
    # Component 2 boundaries
    B_left = x2
    B_right = x2 + w2
    B_bottom = y2
    B_top = y2 + h2
    
    # Check for overlap
    overlap = not (
        A_right <= B_left or
        A_left >= B_right or
        A_bottom >= B_top or
        A_top <= B_bottom
    )
    
    return overlap
   

def overlap_count(chromosome):
    count = 0
    items = list(chromosome.items())
    #print ("i",items)
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if has_overlap(items[i], items[j]):
                count += 1
    return count

def total_wiring(chromosome):
    total = 0
    for c1, c2 in connetion:
        x1, y1 = center(*chromosome[c1], *components[c1])
        x2, y2 = center(*chromosome[c2], *components[c2])
        total += euclidean((x1, y1), (x2, y2))
    return total

def fitness(chromosome):
    overlap = overlap_count(chromosome)
    wire = total_wiring(chromosome)
    area = bounding_box(chromosome)
    return -(alpha * overlap + beta * wire + gamma * area)

def generate_chromosome():
    chrom = {}
    for name in component_name:
        w, h = components[name]
        x = random.randint(0, gride_size - w)
        y = random.randint(0, gride_size - h)
        chrom[name] = (x, y)
    #print(f"Generated random chromosome: {chrom}") 
    return chrom

def crossover(pa1, pa2):
    point = random.randint(1, len(component_name)-1)
    child1 = {}
    child2 = {}
    crossover_point = random.randint(1, len(pa1) - 1)
    p1=[pa1[name] for name in component_name]
    p2=[pa2[name] for name in component_name]
        
    child1 = p1[:crossover_point] + p2[crossover_point:]
    child2 = p2[:crossover_point] + p1[crossover_point:]
    child_dict1 = {i: j for i,j in zip(component_name, child1)}
    child_dict2 = {i: j for i,j in zip(component_name, child2)}
    
    return child_dict1, child_dict2



def mutate(chromosome):
    if random.random() < mutation_rate:
        name = random.choice(component_name)
        w, h = components[name]
        x = random.randint(0, gride_size - w)
        y = random.randint(0, gride_size - h)
        chromosome[name] = (x, y)

def geneticai():
    population = [generate_chromosome() for _ in range(populationlen)]
    best = None
    elite=[]
    for crom in population:
        fit=fitness(crom)
        elite.append((crom, fit))
    best = elite[0] #To Compare with the first item
    for item in elite:
     if item[1] > best[1]:
        best = item
        
        #print(f"Gen {item}: Best Fitness = {best[1]:.2f}")

    new_pop = [best[0]]  # elitism
    print(f"new_pop: {new_pop}")
    while len(new_pop) < populationlen:
        p1, p2 = random.sample(elite[:4], 2)  # top 4 tournament
        child1, child2 = crossover(p1[0], p2[0])
        mutate(child1)
        mutate(child2)
        new_pop.extend([child1, child2])
    population = new_pop[:populationlen]
    #print (new_pop)
    final = best[0]
   
    print("\nBest Layout:")
    for name, pos in final.items():
        print(f"{name}: {pos}")
    print(f"Total Fitness: {best[1]:.2f}")
    print(f"Total Wiring Length: {total_wiring(final):.2f}")
    print(f"Total Bounding Area: {bounding_box(final):.2f}")
    print(f"Overlap Count: {overlap_count(final)}")

geneticai()

##########task 2######33

gride_size = 25
populationlen = 6
genloop = 15
mutation_rate = 0.1
alpha = 1000  
beta = 2     
gamma = 1    


components = {
    "ALU": (5, 5),
    "Cache": (7, 4),
    "Control": (4, 4),
    "Register": (6, 6),
    "Decoder": (5, 3),
    "Floating": (5, 5)
}

component_name = list(components.keys())
connetion = [
    ("Register", "ALU"),
    ("Control", "ALU"),
    ("ALU", "Cache"),
    ("Register", "Floating"),
    ("Cache", "Decoder"),
    ("Decoder", "Floating")
]
def center(x, y, w, h):
    return (x + w / 2, y + h / 2)

def euclidean(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def bounding_box(chromosome):
    xs = [x for x, y in chromosome.values()]
    ys = [y for x, y in chromosome.values()]
    x_max = max(x + components[name][0] for name, (x, y) in chromosome.items())
    y_max = max(y + components[name][1] for name, (x, y) in chromosome.items())
    x_min = min(xs)
    y_min = min(ys)
    return (x_max - x_min) * (y_max - y_min)

def has_overlap(a, b):
    (x1, y1), (x2, y2) = a[1], b[1]
    w1, h1 = components[a[0]]
    w2, h2 = components[b[0]]
    A_left = x1
    A_right = x1 + w1
    A_bottom = y1
    A_top = y1 + h1
    
    # Component 2 boundaries
    B_left = x2
    B_right = x2 + w2
    B_bottom = y2
    B_top = y2 + h2
    
    # Check for overlap
    overlap = not (
        A_right <= B_left or
        A_left >= B_right or
        A_bottom >= B_top or
        A_top <= B_bottom
    )
    
    return overlap

def overlap_count(chromosome):
    count = 0
    items = list(chromosome.items())
    
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if has_overlap(items[i], items[j]):
                count += 1
    return count

def total_wiring(chromosome):
    total = 0
    for c1, c2 in connetion:
        x1, y1 = center(*chromosome[c1], *components[c1])
        x2, y2 = center(*chromosome[c2], *components[c2])
        total += euclidean((x1, y1), (x2, y2))
    return total

def fitness(chromosome):
    overlap = overlap_count(chromosome)
    wire = total_wiring(chromosome)
    area = bounding_box(chromosome)
    return -(alpha * overlap + beta * wire + gamma * area)

def generate_chromosome():
    chrom = {}
    for name in component_name:
        w, h = components[name]
        x = random.randint(0, gride_size - w)
        y = random.randint(0, gride_size - h)
        chrom[name] = (x, y)
    #print(f"Generated random chromosome: {chrom}")  # Debugging output
    return chrom

def two_point_crossover(p1, p2):
    ind1 = random.randint(0, len(component_name)-2)
    ind2 = random.randint(ind1+1, len(component_name)-1)
    plist1= [p1[name] for name in component_name]
    plist2= [p2[name] for name in component_name]
    childlist1= plist1[:ind1] + plist2[ind1:ind2] + plist1[ind2:]
    childlist2=plist2[:ind1]+plist1[ind1:ind2] + plist2[ind2:]
    child1={i: j for i,j in zip(component_name, childlist1)}
    child2={i: j for i,j in zip(component_name, childlist2)}
    return child1, child2
print("Crossover function created")  # Debugging outp
p01=generate_chromosome()
p02=generate_chromosome()
child1, child2 = two_point_crossover(p01, p02)
print("Child 1:", child1)   
print("Child 2:", child2)