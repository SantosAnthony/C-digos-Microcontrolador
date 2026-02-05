import csv
archiveName = 'Irrigation_Plan.txt'
filtredArchiveName = 'Data_Archive.txt'

filtredLines = []

with open(archiveName, 'r') as f:
    for line in f:
        content = line.split("#")[0].strip().rstrip("|")
        if content != '' and content != '\n':
            filtredLines.append(content)
            


reFiltredLines = []
for line in filtredLines:
    reFiltredLines.append(line.replace("-","/").replace("; ",",").replace(" | ",","))


with open(filtredArchiveName, 'w', newline='') as f:
    writer = csv.writer(f)
    for line in reFiltredLines:
        writer.writerow(line.split(","))
