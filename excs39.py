#Difference between dictioneries and list-- A list is for an ordered list of items. A dictionary (or dict) is for matching some items (called "keys") to other items (called "values"). 
states = {
    'Rajasthan': 'RAJ',
    'Punjab': 'PN',
    'Madhya Pradesh': 'MP',
    'Haryana': 'HR',
    'Bihar': 'BH'
    }

cities = {
    'RAJ': 'Jaipur',
    'BH': 'Patna',
    'HR': 'Mahendragarh',
    }

cities['PN'] = 'Chandigarh'
cities['MP'] = 'Madhya Pradesh'

print '-'*10

print 'RAJ states has:', cities['RAJ']
print 'BH states has:', cities['BH']

print '-'*10
print 'Madhya Pradesh abbriviation is: ',states['Madhya Pradesh']
print 'Haryana abbriviation is: ', states['Haryana']

print '-'*10
print 'Rajasthan has:', cities[states['Rajasthan']]
print'Haryana has:', cities[states['Haryana']]

#print every state abbriviation
print '-'*10
for state, abbrv in states.items(): #.item() is used when we make use of block in a list
    print '%s has the city %s' % (abbrv, state)

#print every city in states
print '-'*10
for state, city in cities.items():
    print '%s city is in %s state.' % (city, state)

#Now do both at the same time
print '-'*10
for state, abbrv in states.items():
    print '%s state has abbreviation  as %s and has city %s' % (state, abbrv, cities[abbrv])

print '-'*10
state = states.get('Texas', None)
if not state:
    print 'Sorry State does not exist'

city = cities.get('TX', 'Does not exist')
print 'The city for the state \'TX\' is: %s' % city
