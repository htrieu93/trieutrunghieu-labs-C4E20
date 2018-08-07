from pymongo import MongoClient
import matplotlib.pyplot as plt

mongo_uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

client = MongoClient(mongo_uri)

db = client.get_default_database()

customers = db['customers']
all_customer = customers.find()

refs = {
    'Word of mouth' : 0,
    'Advertisements' : 0,
    'Events' : 0
}

for customer in all_customer:
    if customer['ref'] == 'wom':
        refs['Word of mouth'] += 1
    elif customer['ref'] == 'ads':
        refs['Advertisements'] += 1
    elif customer['ref'] == 'events':
        refs['Events'] += 1

for key, value in refs.items():
    print('Number of customers by {}: {}'.format(key, value))

plt.pie(refs.values(), labels = refs.keys(), autopct = '%.1f%%')
plt.axis('equal')

plt.show()

