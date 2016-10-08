import csv
with open("ingred.txt", "r") as f:
    # reader = csv.reader(f)
    # bigList = list(reader)
    for line in f:
        t_list = eval(line)
        if t_list[4] and (t_list[5] == "MG"):
            print t_list

#print (bigList)
