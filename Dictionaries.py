# discionary = { key:value, key:value,..., key:value}
monthConversions = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'Dec': 'December',
    }

print(monthConversions['Nov'])
print(monthConversions.get('Nov'))
#print(monthConversions['Lov'])     #if we use[], it will cause an erro if the key wasn't there
print(monthConversions.get('Lov'))  #if we use .get, it will display None if the key wasn't there
print(monthConversions.get('Lov', 'Not in a data'))  #if we use .get, it will display 'Not in a data' if the key wasn't there
