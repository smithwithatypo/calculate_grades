# QUIZZES
q1 = 7
q2 = 7
q3 = 6
q4 = 4
q5 = 4
q6 = 8
q7 = 4
q8 = 6
# q9 = 8
# q10 = 8

quizzes = [q1, q2, q3, q4, q5, q6, q7, q8]   # current
# quizzes = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]   # final


# TESTS
test1 = 69
test2 = 70

tests = [test1, test2]


# FINAL
final = 80
final = [final * 2]


# ATTENDANCE BONUS
attendance = 10


# HELPER FUNCTIONS
def avg(a): 
    return sum(a) / len(a)

def drop_lowest(lst):
    lowest = 10
    for num in lst:
        if num < lowest:
            lowest = num
    lst.remove(lowest)
    return sum(lst)

def grade(num):
    if num < 299:
        return "F"
    if num <= 349:
        return "D"
    if num <= 399:
        return "C"
    if num <= 449:
        return "B"
    if num <= 500:
        return "A"


# OUTPUT
total = drop_lowest(quizzes) + sum(tests) + sum(final) + attendance
print("Final grade is", total, "which is a", grade(total))