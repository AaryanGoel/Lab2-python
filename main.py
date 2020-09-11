def getLetterGrade(newGrade1):

    numGrade = newGrade1
    lGrade = ""

    if numGrade >= 93:
        lGrade = "A"
    elif numGrade >= 90:
        lGrade = "A-"
    elif numGrade >= 87:
        lGrade = "B+"
    elif numGrade >= 83:
        lGrade = "B"
    elif numGrade >= 80:
        lGrade = "B-"
    elif numGrade >= 77:
        lGrade = "C"
    elif numGrade >= 60:
        lGrade = "D"
    else:
        lGrade = "F"
    return lGrade


def run():
    Ygrade = float(input("Enter your CMPSC 131 grade: "))
    output = getLetterGrade(Ygrade)
    print(f"Your letter grade for CMPSC 131 is {output}.")


if __name__ == "__main__":
    run()
