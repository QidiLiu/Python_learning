# Note: walrus_operator := is only be used in Python3.8 or later
# 1. Difference between while and do...while

# while
n_1 = 0
while(n_1<3):
    print('while:', n_1) # 0,1,2
    n_1 += 1

# do...while with walrus_operator
n_2 = 0
while((n_2:=n_2+1)<3): # Brackets must be added here
    print('do...while', n_2) # 1,2

# 2. Used in endless loop
while(answer:=input('Do you love me?') != ('yes' or 'y')):
    continue

# 3. List comprehension

def qualified(n):
    if(n>=60):
        return True
    else:
        return False
# without walrus_operator
scores = [22, 54, 75, 89]
qualified_scores = [
    qualified(n)
    for n in scores
    if qualified(n)
]

print(qualified_scores)
