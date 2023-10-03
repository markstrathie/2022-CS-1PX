import matplotlib.pyplot as plt

# plan for data structure: a list of dictionaries so for the first line:
[{'price': 31.2, 'cost': 27.8, 'monthlyProduction': 32889042, 'month': 2, 'region': 'Ashire'}]

def readData(filename):
  myList = []
  try: 
    for line in open(filename):
      split = line.strip().split(',')
      price = float(split[0])
      cost = float(split[1])
      monthlyProd = int(split[2])
      month = int(split[3])
      region = split[4]
      record = {'price': price, 'cost': cost, 'monthlyProduction': monthlyProd, 'month': month, 'region': region}
      myList.append(record)
    return myList
  except TypeError:
    print('Incorrect type detected ')
    return myList
  except: 
     print ('unable to parse line ' + line)
     return myList
    #  They are likely to have lots of different solutions here for error checking


def filterByRegion(dataStruct, regionString):
  newList = []
  for record in dataStruct:
    if record['region'] == regionString:
      newList.append(record)
  return newList

def filterByMonth(dataStruct, month):
  newList = []
  for record in dataStruct:
    if record['month'] == month:
      newList.append(record)
  return newList


def getPricesPerUnit(dataStruct):
  listOfPrices = []
  for record in dataStruct:
    listOfPrices.append(record['price'])
  return listOfPrices


def getCostsPerUnit(dataStruct):
  listOfCosts = []
  for record in dataStruct:
    listOfCosts.append(record['cost'])
  return listOfCosts

def getTotalProduction(dataStruct):
  listOfProd = []
  for record in dataStruct:
    listOfProd.append(record['monthlyProduction'])
  return listOfProd


def calculateProfitPerUnit(dataStruct):
  listOfProfits = []
  for record in dataStruct:
    listOfProfits.append(record['price'] - record['cost'])
  return listOfProfits


dataStruct = readData('poturnip.csv')
print(getPricesPerUnit(dataStruct[:3]))
print(getCostsPerUnit(dataStruct[:3]))
print(calculateProfitPerUnit(dataStruct[:3]))

# print(filterByMonth(dataStruct, 10))
print(filterByRegion(dataStruct[:3], 'Cshire'))

plt.scatter(getPricesPerUnit(dataStruct), getCostsPerUnit(dataStruct))
plt.show()
plt.clf()
plt.scatter(getPricesPerUnit(dataStruct), getTotalProduction(dataStruct))
plt.show()
plt.clf()
justAProfit = calculateProfitPerUnit(filterByRegion(dataStruct, 'Ashire'))
plt.hist(justAProfit)
plt.show()
plt.clf()

justBProfit = calculateProfitPerUnit(filterByRegion(dataStruct, 'Bshire'))
plt.hist(justBProfit)
plt.show()
plt.clf()

justCProfit = calculateProfitPerUnit(filterByRegion(dataStruct, 'Cshire'))
plt.hist(justCProfit)
plt.show()
plt.clf()

 # Some of this plotting could sensibly be placed in functions - encourage students to do this if they want to.  

seasonDict = {'winter': [12, 1, 2], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}

def selectOnSeason(listOfMonths, dataStruct):
  newList = []
  for record in dataStruct:
    if record['month'] in listOfMonths:
      newList.append(record)
  return newList

# a more general solution would be to get this list be traversing the data 
regions = {'Ashire', 'Bshire', 'Cshire'}

for region in regions:
  for season in seasonDict:
    subselected = selectOnSeason(seasonDict[season], filterByRegion(dataStruct, region))
#     displaying instead of saving is perfectly fine
    plt.boxplot(calculateProfitPerUnit(subselected))
    plt.savefig(str(region) + "_" + str(season) + ".pdf")
    plt.clf()
# 