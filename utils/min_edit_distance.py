def med_function(word1, word2, show_matrix):

    rows = len(word1)+1 
    cols = len(word2)+1

    distance = [
        [0 for x in range(cols)] 
        for x in range(rows)]

    for i in range(1, rows):
        distance[i][0] = i

    for j in range(1, cols):
        distance[0][j] = j
        
    for col in range(1, cols):
        for row in range(1, rows):
            if word1[row-1] == word2[col-1]:
                sub_cost = 0
            else:
                sub_cost = 1
            distance[row][col] = min(distance[row-1][col] + 1,      
                                     distance[row][col-1] + 1,    
                                     distance[row-1][col-1] + sub_cost)
    
    if show_matrix:
        print("The MED matrix between " + word1 + " and " + word2 + " is: ")
        for r in range(rows):
            print(distance[r])
    
    return distance[row][col]

