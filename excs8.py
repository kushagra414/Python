string4 = '%r, %r, %r, %r'
print string4 % (1, 2, 3, 4)
print string4 % ('one', 'two', 'three', 'four')
# print string4 % ('only one string') - gives error
print string4 % (True, False, True, False) # Can use without '' as they are keywords
print string4 % (string4, string4, string4, string4) # Prints  '%r, %r, %r, %r' 4 times.



