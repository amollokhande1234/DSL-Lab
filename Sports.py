def intersection(l1,l2):
    res = []
    for student in l1:
        if student in l2:
            res.append(student)
    return res

cricket=[1,2,3,4,5,6,7]
badminton=[2,5,73,10]
football=[2,23,5,10,3]

# Question One 
print("Question One ")
print(intersection(cricket, football))

# Second 
def union(l1,l2):
    res=l2.copy()
    for student in l1:
        if not student in l2:
            res.append(student)
    return res

def diff(l1,l2):
    res=[]
    for student in l1:
        if not student in l2:
            res.append(student)
    return res

u=union(cricket, badminton)
i=intersection(cricket, badminton)
print("Question 2")
print(diff(u,i))

# Question 3
cricketandfootball=diff(cricket, badminton)
print("Question 3")
print(diff(cricketandfootball,football))

#Question 4
def fandb(l1,l2):
    res=[]
    for student in l1:
        if student in l2:
            res.append(student)
    return res
fandb=union(cricket,football)
print("Questin 4")
print(diff(fandb,badminton))