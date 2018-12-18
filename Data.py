import csv
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('TCBT.csv', sep=',', encoding='CP866')

napravlenie = df.values[:, 0]
period = df.values[:, 1]
country = df.values[:, 2]
tnved = df.values[:, 3]
cost = df.values[:, 5]
netto = df.values[:, 6]

index = []
for i in range(len(tnved)):
    if tnved[i] == '2401' and napravlenie[i] == 'ИМ':
        index.append(i)

newcountry = []
for i in index:
    newcountry.append(country[i])

newperiod = []
for i in index:
    newperiod.append(period[i])

newnetto = []
for i in index:
    newnetto.append(netto[i] / 1000)

newcost = []
for i in index:
    newcost.append(cost[i] / 1000)

uniquecountry = []
place = []
places = []
for i in newcountry:
    if i not in uniquecountry:
        uniquecountry.append(i)
for j in range(len(uniquecountry)):
    for i in range(len(newcountry)):
        if uniquecountry[j] == newcountry[i]:
            place.append(i)
    places.append(place)
    place = []

# Создаем словари с количеством импорта по годам для каждой страны
netto_2013 = []
netto_2014 = []
netto_2015 = []
netto_2016 = []
n2013 = n2014 = n2015 = n2016 = 0
for i in places:
    for j in i:
        if newperiod[j] == 2013:
            n2013 += newnetto[j]
        elif newperiod[j] == 2014:
            n2014 += newnetto[j]
        elif newperiod[j] == 2015:
            n2015 += newnetto[j]
        elif newperiod[j] == 2016:
            n2016 += newnetto[j]
    netto_2013.append(n2013)
    netto_2014.append(n2014)
    netto_2015.append(n2015)
    netto_2016.append(n2016)
    n2013 = n2014 = n2015 = n2016 = 0

dic2013 = {netto_2013[i]: uniquecountry[i] for i in range(len(netto_2013))}
netto_2013.sort(reverse=True)
largest_import2013 = netto_2013[:10]
largest_dealers2013 = []
for i in largest_import2013:
    largest_dealers2013.append(dic2013[i])

dic2014 = {netto_2014[i]: uniquecountry[i] for i in range(len(netto_2014))}
netto_2014.sort(reverse=True)
largest_import2014 = netto_2014[:10]
largest_dealers2014 = []
for i in largest_import2014:
    largest_dealers2014.append(dic2014[i])

dic2015 = {netto_2015[i]: uniquecountry[i] for i in range(len(netto_2015))}
netto_2015.sort(reverse=True)
largest_import2015 = netto_2015[:10]
largest_dealers2015 = []
for i in largest_import2015:
    largest_dealers2015.append(dic2015[i])

dic2016 = {netto_2016[i]: uniquecountry[i] for i in range(len(netto_2016))}
netto_2016.sort(reverse=True)
largest_import2016 = netto_2016[:10]
largest_dealers2016 = []
for i in largest_import2016:
    largest_dealers2016.append(dic2016[i])

# Создаем словари со стоимостью импорта по годам для каждой страны
cost_2013 = []
cost_2014 = []
cost_2015 = []
cost_2016 = []
c2013 = c2014 = c2015 = c2016 = 0
for i in places:
    for j in i:
        if newperiod[j] == 2013:
            c2013 += newcost[j]
        elif newperiod[j] == 2014:
            c2014 += newcost[j]
        elif newperiod[j] == 2015:
            c2015 += newcost[j]
        elif newperiod[j] == 2016:
            c2016 += newcost[j]
    cost_2013.append(c2013)
    cost_2014.append(c2014)
    cost_2015.append(c2015)
    cost_2016.append(c2016)
    c2013 = c2014 = c2015 = c2016 = 0

dict2013 = {cost_2013[i]: uniquecountry[i] for i in range(len(cost_2013))}
cost_2013.sort(reverse=True)
expensive_cost2013 = cost_2013[:10]
expensive_dealers2013 = []
for i in expensive_cost2013:
    expensive_dealers2013.append(dict2013[i])

dict2014 = {cost_2014[i]: uniquecountry[i] for i in range(len(cost_2014))}
cost_2014.sort(reverse=True)
expensive_cost2014 = cost_2014[:10]
expensive_dealers2014 = []
for i in expensive_cost2014:
    expensive_dealers2014.append(dict2014[i])

dict2015 = {cost_2015[i]: uniquecountry[i] for i in range(len(cost_2015))}
cost_2015.sort(reverse=True)
expensive_cost2015 = cost_2015[:10]
expensive_dealers2015 = []
for i in expensive_cost2015:
    expensive_dealers2015.append(dict2015[i])

dict2016 = {cost_2016[i]: uniquecountry[i] for i in range(len(cost_2016))}
cost_2016.sort(reverse=True)
expensive_cost2016 = cost_2016[:10]
expensive_dealers2016 = []
for i in expensive_cost2016:
    expensive_dealers2016.append(dict2016[i])

# Крупнейшие импортеры табака в Россию (по количеству)
value = 0
values = []
for i in places:
    for j in i:
        value += newnetto[j]
    values.append(value)
    value = 0
dic = {values[i]: uniquecountry[i] for i in range(len(uniquecountry))}
# print(dic)
values.sort(reverse=True)
largest_import = values[:10]
largest_dealers = []
for i in largest_import:
    largest_dealers.append(dic[i])

# Крупнейшие импортеры табака в Россию (по стоимости)
value2 = 0
values2 = []
for i in places:
    for j in i:
        value2 += newcost[j]
    values2.append(value2)
    value2 = 0
dic2 = {values2[i]: uniquecountry[i] for i in range(len(uniquecountry))}
# print(dic2)
values2.sort(reverse=True)
expensive_cost = values2[:10]
expensive_dealers = []
for i in expensive_cost:
    expensive_dealers.append(dic2[i])

# Общий импорт табака в Россию по годам
netto_IM_2013 = netto_IM_2014 = netto_IM_2015 = netto_IM_2016 = 0
for i in range(len(newperiod)):
    if newperiod[i] == 2013:
        netto_IM_2013 += newnetto[i]
    elif newperiod[i] == 2014:
        netto_IM_2014 += newnetto[i]
    elif newperiod[i] == 2015:
        netto_IM_2015 += newnetto[i]
    elif newperiod[i] == 2016:
        netto_IM_2016 += newnetto[i]

all_netto = netto_IM_2013 + netto_IM_2014 + netto_IM_2015 + netto_IM_2016

sort_counries_on_netto = []
percent = []
c = 0
for i in values:
    sort_counries_on_netto.append(dic[i])
    c = float('{:.3f}'.format(i / all_netto * 100))
    percent.append(c)

countries = []
with open('Countries.csv', 'r') as file:
    r = csv.reader(file)
    for line in r:
        countries.append(line)
indx = []
strana = []
for i in range(len(countries)):
    indx.append(countries[i][0])
    strana.append(countries[i][1])
countrydic = {indx[i]: strana[i] for i in range(len(indx))}

sort_contries = []
for i in values:
    sort_contries.append(countrydic[dic[i]])

fixed_values = []
for i in values:
    fixed_values.append(float('{:.4f}'.format(i)))

rating = pd.DataFrame({'Страна': sort_contries, 'Количество, т': fixed_values, '% от всего импорта': percent},
                      index=sort_counries_on_netto)
# print(rating)
# rating.to_csv('Рейтинг.csv', encoding = 'Windows-1251')

# Импорт из Бразилии по годам
periodBR = []
costBR = []
nettoBR = []
for i in range(len(newcountry)):
    if newcountry[i] == 'BR':
        periodBR.append(newperiod[i])
        costBR.append(newcost[i])
        nettoBR.append(newnetto[i])
cost2013 = netto2013 = cost2014 = netto2014 = cost2015 = netto2015 = cost2016 = netto2016 = 0
for i in range(len(periodBR)):
    if periodBR[i] == 2013:
        cost2013 += costBR[i]
        netto2013 += nettoBR[i]
    elif periodBR[i] == 2014:
        cost2014 += costBR[i]
        netto2014 += nettoBR[i]
    elif periodBR[i] == 2015:
        cost2015 += costBR[i]
        netto2015 += nettoBR[i]
    elif periodBR[i] == 2016:
        cost2016 += costBR[i]
        netto2016 += nettoBR[i]

fig = plt.figure()
plt.suptitle('Крупнейшие импортеры табака в Россию по годам')
plt.subplots_adjust(top=0.88, bottom=0.1, left=0.15, right=0.97, hspace=0.55, wspace=0.5)

# 2013
number_one = plt.subplot(221)
plt.bar(largest_dealers2013, largest_import2013, color='#CC6633', zorder=2)
plt.title('2013')
plt.xlabel('Страны')
plt.ylabel('Количество, т')
plt.grid(True)

# 2014
plt.subplot(222, sharey=number_one)
plt.bar(largest_dealers2014, largest_import2014, color='#CC6633', zorder=2)
plt.title('2014')
plt.xlabel('Страны')
plt.ylabel('Количество, т')
plt.grid(True)

# 2015
plt.subplot(223, sharey=number_one)
plt.bar(largest_dealers2015, largest_import2015, color='#CC6633', zorder=2)
plt.title('2015')
plt.xlabel('Страны')
plt.ylabel('Количество, т')
plt.grid(True)

# 2016
plt.subplot(224, sharey=number_one)
plt.bar(largest_dealers2016, largest_import2016, color='#CC6633', zorder=2)
plt.title('2016')
plt.xlabel('Страны')
plt.ylabel('Количество, т')
plt.grid(True)
plt.show()

fig = plt.figure()
plt.suptitle('Крупнейшие импортеры табака в Россию по годам')
plt.subplots_adjust(top=0.88, bottom=0.1, left=0.15, right=0.97, hspace=0.55, wspace=0.5)

# 2013
number_two = plt.subplot(221)
plt.bar(expensive_dealers2013, expensive_cost2013, color='#440000', zorder=2)
plt.title('2013')
plt.xlabel('Страны')
plt.ylabel('Стоимость, $ тыс.')
plt.grid(True)

# 2014
plt.subplot(222, sharey=number_two)
plt.bar(expensive_dealers2014, expensive_cost2014, color='#440000', zorder=2)
plt.title('2014')
plt.xlabel('Страны')
plt.ylabel('Стоимость, $ тыс.')
plt.grid(True)

# 2015
plt.subplot(223, sharey=number_two)
plt.bar(expensive_dealers2015, expensive_cost2015, color='#440000', zorder=2)
plt.title('2015')
plt.xlabel('Страны')
plt.ylabel('Стоимость, $ тыс.')
plt.grid(True)

# 2016
plt.subplot(224, sharey=number_two)
plt.bar(expensive_dealers2016, expensive_cost2016, color='#440000', zorder=2)
plt.title('2016')
plt.xlabel('Страны')
plt.ylabel('Стоимость, $ тыс.')
plt.grid(True)
plt.show()

fig = plt.figure()
plt.bar(largest_dealers, largest_import, color='#CC6633', zorder=2)
plt.title('Крупнейшие импортеры табака в Россию')
plt.xlabel('Страны')
plt.ylabel('Количество, т')
plt.subplots_adjust(left=0.2)
plt.grid(True)
plt.show()

fig = plt.figure()
plt.bar(expensive_dealers, expensive_cost, color='#440000', zorder=2)
plt.title('Крупнейшие импортеры табака в Россию')
plt.xlabel('Страны')
plt.ylabel('Стоимость, $ тыс.')
plt.subplots_adjust(left=0.2)
plt.grid(True)
plt.show()

fig = plt.figure()
years_IM = ['2013', '2014', '2015', '2016']
netto_IM = [netto_IM_2013, netto_IM_2014, netto_IM_2015, netto_IM_2016]
plt.title('Общий импорт табака в Россию по годам')
plt.bar(years_IM, netto_IM, width=0.5, color='#CC6633', zorder=2)
plt.ylabel('Количество табака, т')
plt.subplots_adjust(left=0.2)
plt.grid(True)
plt.show()

fig = plt.figure()
plt.title('Общий импорт табака в Россию по годам')
plt.plot(years_IM, netto_IM, linewidth=2, color="#CC6633", zorder=2)
plt.scatter(years_IM, netto_IM, color="#440000", zorder=3)
plt.ylabel('Количество табака, т')
plt.ylim(0, 300000)
plt.subplots_adjust(left=0.2)
plt.grid(True)
plt.show()

fig = plt.figure()
years = ['2013', '2014', '2015', '2016']
cost_on_years = [cost2013, cost2014, cost2015, cost2016]
netto_on_years = [netto2013, netto2014, netto2015, netto2016]
plt.title('Импорт из Бразилии по годам')
plt.bar([x + 0.05 for x in range(len(years))], cost_on_years,
        width=0.3, color='#440000', label='Стоимость табака, $ тыс.',
        zorder=2)
plt.bar([x + 0.4 for x in range(len(years))], netto_on_years,
        width=0.3, color='#CC6633', label='Количество табака, т',
        zorder=2)
plt.xticks(range(len(years)), years)
plt.subplots_adjust(left=0.18, right=0.93)
plt.legend(loc='upper right')
plt.grid(True)
plt.show()