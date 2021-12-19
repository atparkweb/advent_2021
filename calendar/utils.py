def file_to_list(file_path):
    result = []
    f = open(file_path, "r")
    lines = f.readlines()
    
    for line in lines:
       result.append(int(line)) 
       
    return result
