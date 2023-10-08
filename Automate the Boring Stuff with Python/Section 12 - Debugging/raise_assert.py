# ------------------------------Raise Exceptions------------------------------
# """
# *****************
# *               *
# *               *
# *               *
# *****************
# """
#
# def boxPrint(symbol, width, height):
#     if len(symbol) != 1:
#         raise Exception("'symbol' needs to be a string of length 1")
#     if (width < 2) or (height < 2):
#         raise Exception("'width' and 'height' must be greater or equal to 2")
#     print(symbol * width)
#     for i in range(height - 2):
#         print(symbol + (' ' * (width - 2 ) + symbol))
#     print(symbol * width)
#
#
# boxPrint("*", 15, 5)
# boxPrint("O", 5, 16)
# boxPrint("**", 15, 5)

# ------------------------------Saving error log------------------------------
# import traceback
# try:
#     raise Exception("This is the error message")
# except:
#     error_file = open("error_log.txt", "a")
#     error_file.write(traceback.format_exc())
#     error_file.close()
#     print("The traceback info was written error_log.txt")

# --------------------------------Assert Error--------------------------------
market_2nd = {"ns": "green", "ew": "red"}


def switch_lights(intersection):
    for key in intersection.keys():
        if intersection[key] == "green":
            intersection[key] = "yellow"
        elif intersection[key] == "yellow":
            intersection[key] = "red"
        elif intersection[key] == "red":
            intersection[key] = "green"
    assert "red" in intersection.values(), "Neither lights is red!" + str(
        intersection)


switch_lights(market_2nd)  # Assertion errors are for programmers, to ensure
# bugs are not present if functioning correctly
