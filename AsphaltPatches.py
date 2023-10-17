def solution(road):
    #initializing
    patch_count = 0  
    num_segments = len(road) 
    segment_index = 0 
#Start a loop to iterate through the road segments
    while segment_index < num_segments:  

        if road[segment_index] == "X": 
            patch_count += 1 
            segment_index += 3 

        else:
            segment_index += 1  

    return patch_count 
# Test cases/output
print(solution(".X..X"))  
print(solution("X.XXXXX.X.")) 
print(solution("XX.XXX..")) 
print(solution("XXXX"))  
print(solution('.X...XX')) 
