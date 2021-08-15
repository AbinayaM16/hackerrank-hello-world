if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    

    for name in student_marks:
       if name==query_name:
          le=len(student_marks[name])
          ave=sum(student_marks[name])/le
          print('{:.2f}'.format(ave))
    
