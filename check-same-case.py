def same_case(a, b): 
    if not (a.isalpha() and b.isalpha()):
        return -1
    if (a.islower() and b.islower()) or (a.isupper() and b.isupper()):
        return 1
    return 0
    
    
print(same_case('a', 'g'))  # 1
print(same_case('A', 'C'))  # 1
print(same_case('b', 'G'))  # 0
print(same_case('B', 'g'))  # 0
print(same_case('0', '?'))  # -1