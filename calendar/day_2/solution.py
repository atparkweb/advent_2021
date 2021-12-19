def file_to_list(file_path):
   result = [] 
   f = open(file_path, "r")
   lines = f.readlines()
   
   for line in lines:
       result.append(line)
       
   return result

def run():
    return file_to_list("calendar/day_2/input")
