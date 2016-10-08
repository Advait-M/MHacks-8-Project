import csv
with open("drug.csv", "r") as f:
    reader = csv.reader(f)
    bigList = list(reader)

writeFile= open("output.txt", "w")
writeFile.write(bigList)
