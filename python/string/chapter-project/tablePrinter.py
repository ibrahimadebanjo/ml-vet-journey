tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable():
    colWidths = [0] * len(tableData)
    for y in range(len(tableData[0])):
       for x in range(len(tableData)):
         print(tableData[x][y], end='')
    print()


printTable()
