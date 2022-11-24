# according to the proof of section A, if I see that there are more than n-1 objects in common,
# that means there is a circle - to know if there are objects in common,
# I checked if there is an object whose distribution is different from 0 and 1.
def check_circle(mat) -> bool:
    n = len(mat)
    count = 0
    prev = len(mat[0])
    lst = []
    b = False
    # A list of the sum of the value of each object received by the players
    # to check at the end that the input is correct and the sum of each value is indeed 1
    for i in range(prev):
        lst.append(0)
    for player in range(len(mat)):
        if prev != len(mat[player]):  # Checks that for each player there is a value for all objects
            print("error")
        prev = len(mat[player])
        for num in range(len(mat[player])):
            lst[num] += mat[player][num]
            if mat[player][num] != 0 and mat[player][num] != 1:
                count += 1
            if count > n - 1:
                b = True
        count = 0
    for i in range(len(lst)):  # Checks that the sum of the values of each object is equal to 1
        if lst[i] != 1:
            print("lst[", i, "]=", lst[i], " error")
    return b


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    l1 = [[1, 1, 0.07, 0, 0.6], [0, 0, 0.93, 0.4]]
    print(check_circle(l1))  # =>True
    l2 = [[1, 1, 0.07, 0], [0, 0, 0.93, 0], [0, 0, 0, 1]]
    print(check_circle(l2))  # =>False
    l3 = [[1, 1, 0.07, 0, 0.6], [0, 0, 0.93, 0, 0.2], [0, 0, 0, 1, 0.2]]
    print(check_circle(l3))  # =>False
    l4 = [[1, 1, 0.07, 0, 0, 0], [0, 0, 0.93, 0, 0, 0], [0, 0, 0, 1, 0.5, 0], [0, 0, 0, 0, 0.5, 1]]
    print(check_circle(l4))  # =>False
    l5 = [[1, 1, 0.07, 0.3, 0, 0], [0, 0, 0.93, 0.5, 0, 0], [0, 0, 0, 0.1, 0.5, 0], [0, 0, 0, 0.1, 0.5, 1]]
    print(check_circle(l5))  # =>False
    l6 = [[0.3, 1, 0.07, 0.3, 0, 0], [0.4, 0, 0.93, 0.5, 0, 0], [0.3, 0, 0, 0.1, 0.5, 0], [0, 0, 0, 0.1, 0.5, 1]]
    print(check_circle(l6))  # =>False
    l7 = [[0.3, 1, 0.07, 0.3, 0, 0.5], [0.4, 0, 0.93, 0.5, 0, 0.3], [0.3, 0, 0, 0.1, 0.5, 0.1],
          [0, 0, 0, 0.1, 0.5, 0.1]]
    print(check_circle(l7))  # =>True
    l8 = [[0.3, 1, 0.07, 0.3, 0, 0.5, 1], [0.4, 0, 0.93, 0.5, 0, 0.3, 0], [0.3, 0, 0, 0.1, 0.5, 0.1, 0],
          [0, 0, 0, 0.1, 0.5, 0.1, 0]]
    print(check_circle(l8))  # =>True

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
