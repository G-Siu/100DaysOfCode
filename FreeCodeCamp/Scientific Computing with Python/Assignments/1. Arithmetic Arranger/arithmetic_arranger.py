def arithmetic_arranger(problems, answer=False):
    top_row = list()
    sign = list()
    bottom_row = list()
    top_length = list()
    bottom_length = list()
    dash_length = list()
    answers = list()
    for problem in problems:
        separate = problem.split()
        top_row.append(separate[0])
        sign.append(separate[1])
        bottom_row.append(separate[2])
        top_length.append(len(separate[0]))
        bottom_length.append(len(separate[2]))

        # Return error if non digit character found
        if separate[0].isdigit() is False or separate[2].isdigit() is False:
            return "Error: Numbers must only contain digits."

        # Check operands
        if separate[1] == "+":
            calculate = int(separate[0]) + int(separate[2])
            answers.append(str(calculate))
        elif separate[1] == "-":
            calculate = int(separate[0]) - int(separate[2])
            answers.append(str(calculate))
        # Return error if / or x operand
        elif separate[1] == "/" or separate[1] == "x":
            return "Error: Operator must be '+' or '-'."
    for i in range(len(top_length)):
        # Error for max operand of over four digits
        if top_length[i] > 4 or bottom_length[i] > 4:
            return "Error: Numbers cannot be more than four digits."
        # Format mathematics rows
        if top_length[i] > bottom_length[i]:
            difference = top_length[i] - bottom_length[i]
            top_row[i] = " " * 2 + top_row[i] + " " * 4
            bottom_row[i] = (sign[i] + " " + " " * difference + bottom_row[i] +
                             " " * 4)
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
        answers[i] = (" " * ((len(dash_length[i]) - 4) - len(answers[i])) +
                      answers[i] + " " * 4)
    # Join everything together
    arranged_problems = ("".join(top_row).rstrip() + "\n" + "".join(
        bottom_row).rstrip() + "\n" +
                         "".join(dash_length)).rstrip()

    if answer:
        arranged_problems += "\n" + "".join(answers)
    # Return error if more than five problems entered
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        return arranged_problems.rstrip()
