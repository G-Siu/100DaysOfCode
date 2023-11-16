import pandas

PFC = "Primary Fur Color"

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = len(data[data[PFC] == "Gray"])
red = len(data[data[PFC] == "Cinnamon"])
black = len(data[data[PFC] == "Black"])


data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [gray, red, black]
}
DF = pandas.DataFrame(data_dict)
DF.to_csv("squirrel_count.csv")
