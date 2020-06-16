import csv
from matplotlib import pyplot as plt 

#Чтение максимальных температур из файла

filename = 'sitka_weather_07-2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)
        
    
    print(highs)

#Наекскние данных на диаграмму.
fig = plt.figure(dpi=128, figsize = (10, 6))
plt.plot(highs, c = 'red')

# Форматирование диаграммы.
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize = 16)
plt.ylabel("Temperature(F)", fontsize = 16)
plt.tick_params(axis='both', which='major', labelsize=16)


plt.show()

    #for index, column_header in enumerate(header_row):
    #    print(index, column_header)
