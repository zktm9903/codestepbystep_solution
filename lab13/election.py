def election():
    file_name = input('Input file? ')

    f = open(file_name, 'r')
    lines = f.readlines()
    candidate1 = 0
    candidate2 = 0

    for line in lines:
        votes = line.split(' ')
        vote1 = int(votes[1])
        vote2 = int(votes[2])
        
        if vote1 == vote2:
            continue
        if vote1 > vote2:
            candidate1 += int(votes[3])
        else:
            candidate2 += int(votes[3])

    print('Candidate 1:', candidate1 ,'votes')
    print('Candidate 2:', candidate2 ,'votes')

    f.close()