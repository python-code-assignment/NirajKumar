"""
    This module basically to calculate the
    studen's grade based on their average
    percentage
"""

KATRINA = {
    "name": "Katrina Kaif",
    "score": [80, 50, 40, 81, 63]
}

DEEPIKA = {
    "name": "Deepika Padukon",
    "score": [77, 82, 23, 39, 74]
}

NORAH = {
    "name": "Norah Fatehi",
    "score": [67, 55, 81, 21, 65]
}

SHRADDHA = {
    "name": "Shraddha kapoor",
    "score": [29, 89, 60, 56, 74]
}

PRIYANKA = {
    "name": "Priyanka Chopra",
    "score": [99, 88, 75, 85, 77]
}


def calculate_total_average(students):
    """ calculates the average of each students"""
    total_average = get_average(students["score"])
    return total_average


def get_average(marks):
    """
        calculates the total marks
        calculates the average
    """
    total_sum = sum(marks)
    total_sum = float(total_sum)
    return total_sum / len(marks)


def assign_grade(score):
    """ assigns grades based on the score """
    if score >= 80 and score <= 95:
        return "A"
    elif score >= 60 and score <= 80:
        return "B"
    else:
        return "C"


ALLSTUDENTS = [KATRINA, DEEPIKA, NORAH, SHRADDHA, PRIYANKA]

for i in ALLSTUDENTS:
    print("\nName: ", i["name"])
    print("-------------------------------------")
    print("Average Marks is : %s" %
          (calculate_total_average(i)), "%")

    print("Grade \t\t : %s " %
          (assign_grade(calculate_total_average(i))))
    print()
