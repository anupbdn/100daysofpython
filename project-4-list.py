subjects = ['physics', 'calculus', 'poetry', 'history']

grades = [98, 97, 85, 88]
subjects.append('computer science')
grades.append(100)
gradebook = list(zip(subjects, grades))
gradebook.append(('visual arts', 93))



print(gradebook)
