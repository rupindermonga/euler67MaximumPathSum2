def ReadingFile():
    #n = open("p067_triangle.txt","r")
    n = []
    for eachLine in open("p067_triangle.txt", "r"):
        n.append(eachLine.split())
    return n

def convert():
    n = ReadingFile()
    n = [[int(j) for j in i] for i in n]
    return n

def MaxPathSum2():
    n = convert()
    final_list = n[len(n)-1]
    
    for eachRow in range(len(n)-1,0, -1):
        new_list = []
        for eachElement in range(len(n[eachRow])-1):
            new_list.append(max(final_list[eachElement], final_list[eachElement+1])+n[eachRow-1][eachElement])
        final_list = new_list
    return max(final_list)

final = MaxPathSum2()
print(final)
