######task1##########3
def calculate_utility(gene_sequence, target, weights):
    """Calculate the utility score for a gene sequence against target."""
    max_len = max(len(gene_sequence), len(target))
    score = 0
    
    for i in range(max_len):
        if i < len(gene_sequence):
            gene_ascii = ord(gene_sequence[i])
        else:
            gene_ascii = 0
        if i < len(target):
             target_ascii = ord(target[i])
        else: target_ascii= 0
        if i < len(weights) :
            weight = weights[i] 
        else: weight= 1
        score += weight * abs(gene_ascii - target_ascii)
    
    return -score  

def minimax_alpha_beta(pool, gene_sequence, target, weights, is_maximizing, alpha, beta):
    
    if not pool:
        return calculate_utility(gene_sequence, target, weights), gene_sequence
    
    if is_maximizing:
        alpha = float('-inf')
        best_sequence = gene_sequence
    
        #new_pool=[]
        for i, nucleotide in enumerate(pool):
            #print(i, nucleotide)
            new_pool=[]
            for j in range(len(pool)):
                if j != i:
                    new_pool.append(pool[j])
            new_sequence = gene_sequence + nucleotide
            score, sequence = minimax_alpha_beta(new_pool, new_sequence, target, weights, False, alpha, beta)
            
            if score > alpha:
                alpha = score
                best_sequence = sequence
            
            alpha = max(alpha, score)
            if beta <= alpha:
                break  
        
        return alpha, best_sequence
    
    else:  
        beta = float('inf')
        best_sequence = gene_sequence
        
        for i, nucleotide in enumerate(pool):
            new_pool=[]
            for j in range(len(pool)):
                if j != i:
                    new_pool.append(pool[j])
            new_sequence = gene_sequence + nucleotide
            
            score, sequence = minimax_alpha_beta(new_pool, new_sequence, target, weights, True, alpha, beta)
            
            if score < beta:
                beta = score
                best_sequence = sequence
            
            beta = min(beta, score)
            if beta <= alpha:
                break  
        
        return beta, best_sequence

pool=input("Enter the pool of nucleotides: ")
target = input("Enter the target gene sequence: ")
student_id_str = input("Enter the student ID digits: ")
pool = pool.split(',')
student_id = list(map(int, student_id_str.split()))
target_len = len(target)
weights = student_id[-target_len:] if len(student_id) >= target_len else student_id
best_score, best_sequence = minimax_alpha_beta( pool, "", target, weights, True, float('-inf'), float('inf'))

print(f"Best gene sequence generated: {best_sequence}")
print(f"Utility score: {best_score}")

###########task2#########
'''
def calculate_utility(gene_sequence, target, weights, student_id):
   
    max_len = max(len(gene_sequence), len(target))
    score = 0
    firsttwodigit=int(str(student_id[0]) + str(student_id[1]))
    booster=firsttwodigit/100
    effective_weights = weights.copy()
    s_position = -1  
    if 'S' in gene_sequence:
        for i in range(len(gene_sequence)):
            if "S" ==gene_sequence[i]:
                s_position = i
        
        for j in range(s_position, len(effective_weights)):
                    effective_weights[j] *= booster
            

    for i in range(max_len):
        gene_ascii = ord(gene_sequence[i]) 
        if i < len(target) :
            target_ascii = ord(target[i])
        else: target_ascii=0
        if i < len(effective_weights):
            weight = effective_weights[i]
        else:
            weight = 1
        
        
       
        score += weight * abs(gene_ascii - target_ascii)
    
    return -score  # Negative 

def minimax_alpha_beta(pool, gene_sequence, target, weights, student_id, is_maximizing, alpha, beta, depth=0):
    
    
    if not pool:
        return calculate_utility(gene_sequence, target, weights, student_id), gene_sequence
    
    if is_maximizing:
        alpha = float('-inf')
        best_sequence = gene_sequence
        
        for i, nucleotide in enumerate(pool):
           
            new_pool=[]
            for j in range(len(pool)):
                if j != i:
                    new_pool.append(pool[j])
         
            new_sequence = gene_sequence + nucleotide
            score, sequence = minimax_alpha_beta(
                new_pool, new_sequence, target, weights, student_id, False, alpha, beta, depth + 1
            )
            
            if score > alpha:
                alpha = score
                best_sequence = sequence
            
            alpha = max(alpha, score)
            if beta <= alpha:
                break 
        
        return alpha, best_sequence
    
    else:  
        beta = float('inf')
        best_sequence = gene_sequence
        
        for i, nucleotide in enumerate(pool):
            
            new_pool=[]
            for j in range(len(pool)):
                if j != i:
                    new_pool.append(pool[j])
           
            new_sequence = gene_sequence + nucleotide
            
           
            score, sequence = minimax_alpha_beta(
                new_pool, new_sequence, target, weights, student_id, True, alpha, beta, depth + 1
            )
            
            if score <beta:
                beta= score
                best_sequence = sequence
            
            beta = min(beta, score)
            if beta <= alpha:
                break  
        
        return beta, best_sequence

def get_decision(pool, target, student_id, task_version=1):
       
    target_len = len(target)
    if len(student_id) >= target_len:
        weights = student_id[-target_len:]
    else: weights= student_id
    
    if task_version == 1:
       
        best_score, best_sequence = minimax_alpha_beta(
            pool, "", target, weights, student_id, True, float('-inf'), float('inf')
        )
        return best_sequence, best_score
    
    else: 
        pool_without_s = [n for n in pool if n != 'S']

        score_without_s, gene_sequence_without_s = minimax_alpha_beta(
            pool_without_s, "", target, weights, student_id, True, float('-inf'), float('inf')
        )

        score_with_s, gene_sequence_with_s = minimax_alpha_beta(
            pool, "", target, weights, student_id, True, float('-inf'), float('inf')
        )

        if score_with_s > score_without_s:
            decision = "YES"
            return decision, gene_sequence_with_s, score_with_s
        else:
            decision = "NO"
            return decision, gene_sequence_with_s, score_with_s

    # Get user input
pool_input = input("Enter nucleotides pool : ").strip()
target_input = input("Enter target gene sequence: ").strip()
sid_input = input("Enter student ID : ").strip()

pool = pool_input.split(',')
student_id = list(map(int, sid_input.split()))
pool=pool+["S"]
    
if "S" in pool_input:
   
   decision,best_sequence, utility_score = get_decision(pool, target_input,student_id, task_version=2)
   print(decision)
else:
    best_sequence, utility_score = get_decision(pool, target_input,student_id, task_version=1)
    print("No")
print("With special nucleotide")
print(f"Best gene sequence generated: {best_sequence}")
print(f"Utility score: {utility_score}")
'''