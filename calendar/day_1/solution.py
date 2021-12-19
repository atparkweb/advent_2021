from ..utils import file_to_list

def count_increase(input):
    count = 0
    i, j = 0, 1
    
    while j < len(input):
        if input[j] > input[i]:
            count += 1
        i += 1
        j += 1
    
    return count

def run():
    return count_increase(file_to_list("calendar/day_1/input"))
