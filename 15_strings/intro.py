"""
Simple Algorithm
"""
str1 = 'Hello World! '
str2 = 'Python Programming'

print ('str1 ', str1)
print ('str2 ', str2)

# accessing values
print (str1[0])
print (str1[2:7])
print (str1[2:])
print (str1 * 2)
print (str1 + 'TEST')

# updating
print ('Updated values: ', str1[:6] + 'Python')

# formatting
print ('My name is %s and weight is %d kg!' % ('Zara', 21))

# triple quotes
paragraph_str = """ This is really
a long paragraph,
it has so many lines
"""
print(paragraph_str)

# unicode strings
print ('capitalize: ', str1.capitalize())
print ('l count: ',str1.count('l'))

# import base64
# str3 = 'come'
# str3 = str3.encode('base64','strict')
# print('Decoded: ',str3.decode(encoding='UTF-8',errors='strict'))

print ('find world: ',str1.find('World'))
print ('find prog', str2.find('Prog'))
print ('lower: ',str1.lower())
print ('lower: ',str1.upper())