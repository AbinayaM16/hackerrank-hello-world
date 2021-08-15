if __name__ == '__main__':
    c=[]
    d=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        c.append([name,score])
        d.append(score)
        
    studentlist=sorted(c)
    secondscore=sorted(set(d))[1]

    for student,mark in studentlist:
        if mark==secondscore:
            print(student)
    
