import csv

def export_csv(events):
    fields = []
    with open('exports/scenes.csv', 'a+') as csvFile:
        for row in events:
            fields.append(row)
            
        writer = csv.writer(csvFile)
        writer.writerows(fields)
    csvFile.close()    
