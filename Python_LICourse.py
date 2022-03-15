# all(iterable)
print(all(['r', '1', []]))
print(all(['2', '']))
print(all(['h', 0]))
print(all(['h', {}]))
print(all([0]))
print(all(['']))
print('----')
print(all([]))    #True
print(all({}))    #True
print(all(''))    #True
print('----')
print(all('0'))
print(all(['h', '0', 3]))