def file_to_list(file_path):
    result = []
    f = open(file_path, "r")
    lines = f.readlines()
    
    for line in lines:
       result.append(int(line)) 
       
    return result

def count_increase(input):
    count = 0
    i = 0
    
    while i + 3 < len(input):
        m1 = input[i] + input[i + 1] + input[i + 2]
        m2 = m1 - input[i] + input[i + 3]
        if m2 > m1:
            count += 1
        i += 1
    
    return count

def run():
    return count_increase(file_to_list("calendar/day_1/input"))
