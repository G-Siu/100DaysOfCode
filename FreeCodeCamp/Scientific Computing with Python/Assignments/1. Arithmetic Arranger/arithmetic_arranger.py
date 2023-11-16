def arithmetic_arranger(problems, answer=False):
    top_row = list()
    sign = list()
    bottom_row = list()
    top_length = list()
    bottom_length = list()
    dash_length = list()
    answers = list()
    for problem in problems:
        seperate = problem.split()
        top_row.append(seperate[0])
        sign.append(seperate[1])
        bottom_row.append(seperate[2])
        top_length.append(len(seperate[0]))
        bottom_length.append(len(seperate[2]))
        if seperate[1] == "+":
            calculate = int(seperate[0]) + int(seperate[2])
            answers.append(str(calculate))
        elif seperate[1] == "-":
            calculate = int(seperate[0]) - int(seperate[2])
            answers.append(str(calculate))
    for i in range(len(top_length)):
        # Error for max operand of over four digits
        if top_length[i] > 4 or bottom_length[i] > 4:
            raise ValueError("Error: Numbers cannot be more than four digits.")
        if top_length[i] > bottom_length[i]:
            difference = top_length[i] - bottom_length[i]
            top_row[i] = " " * 2 + top_row[i] + " " * 4
            bottom_row[i] = sign[i] + " " + " " * difference + bottom_row[i] + " " * 4
            dash_length.append("-" * 2 + "-" * top_length[i] + " " * 4)
        elif bottom_length[i] > top_length[i]:
            difference = bottom_length[i] - top_length[i]
            top_row[i] = " " * 2 + " " * difference + top_row[i] + " " * 4
            bottom_row[i] = sign[i] + " " + bottom_row[i] + " " * 4
            dash_length.append("-" * 2 + "-" * bottom_length[i] + " " * 4)
        else:
            top_row[i] = " " * 2 + top_row[i] + " " * 4
            bottom_row[i] = sign[i] + " " + bottom_row[i] + " " * 4
            dash_length.append("-" * 2 + "-" * top_length[i] + " " * 4)
        answers[i] = (" " * ((len(dash_length[i]) - 4) - len(answers[i])) + answers[i] + " " * 4)
    # Raise error if more than five problems entered
    if len(problems) > 5:
        raise ValueError("Error: Too many problems.")
        
    arranged_problems = "".join(top_row) + "\n" + "".join(bottom_row) + "\n" + "".join(dash_length)
    if answer == True:
        arranged_problems += "\n" + "".join(answers)
    return arranged_problems