def file_to_list(file_path):
   result = [] 
   f = open(file_path, "r")
   lines = f.readlines()
   
   for line in lines:
       [direction, move_str] = line.split()
       result.append([direction, int(move_str)])
       
   return result

def run():
   h = 0;
   v = 0;

   lines = file_to_list("calendar/day_2/input")
   for [direction, n] in lines:
      if direction == "forward":
         h += n
      elif direction == "up":
         v -= n
      elif direction == "down":
         v += n
      else:
         raise "Not a valid direction"
   
   return [h, v]
