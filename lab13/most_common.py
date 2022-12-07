def most_common(file_name):
    rank = {}
    f = open(file_name, 'r')
    lines = f.readlines()
    
    for line in lines:
        line = line.strip("\n")
        names = line.split(' ')
        for name in names:
            if len(name) == 0:
                continue

            if name in rank:
                rank[name] += 1
            else:
                rank[name] = 1
     
    f.close()
    
    print(rank)
    
    sortedRank = sorted(rank.items(), key=lambda x:x[1])
    print(sortedRank)
    
    maxNum = sortedRank[len(sortedRank)-1][1]
    
    for count in sortedRank:
        if count[1] == maxNum:
            return count[0]
    return ''