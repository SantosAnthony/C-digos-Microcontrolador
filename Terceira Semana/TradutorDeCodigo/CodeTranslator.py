import csv
archiveName = 'Irrigation_Plan.txt'
filtredArchiveName = 'Data_Archive.txt'

filtredLines = []

with open(archiveName, 'r') as f:
    for line in f:
        content = line.split("#")[0].strip().rstrip("|")
        if content != '' and content != '\n':
            contentInfo = content.split(" | ")
            date = contentInfo[0].split("-")

            newDate = "-".join(reversed(date))
            contentInfo[0] = newDate
            
            stringInfo = ",".join(contentInfo).replace(" ","").replace("-","/").replace(";",",").replace(" | ",",")
            filtredLines.append(stringInfo)

with open(filtredArchiveName, 'w', newline='') as f:
    writer = csv.writer(f)
    for line in filtredLines:
        writer.writerow(line.split(","))

