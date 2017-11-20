import const
#print(const.test)#AttributeError: '_const' object has no attribute 'test'
const.test = "Test1"
print(const.test)
const.test = "Test2"
print(const.test)

