def med_function(word1, word2):
    rows = len(word1) + 1
    cols = len(word2) + 1

    distance = [
        [0 for x in range(cols)]
        for x in range(rows)]

    for i in range(1, rows):
        distance[i][0] = i

    for j in range(1, cols):
        distance[0][j] = j

    for col in range(1, cols):
        for row in range(1, rows):
            if word1[row - 1] == word2[col - 1]:
                cost = 0
            else:
                cost = 1
            distance[row][col] = min(distance[row - 1][col] + 1,
                                     distance[row][col - 1] + 1,
                                     distance[row - 1][col - 1] + cost)

    print("The MED matrix between " + word1 + " and " + word2 + " is: ")

    for r in range(rows):
        print(distance[r])

    print()
    print("The MED between " + word1 + " and " + word2 + " is: ", )

    return distance[row][col]
