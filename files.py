#   Files
#   Non-volatile in nature

#       Syntax for the open() method
#       file object = open(file_name, access_mode)

path = 'Kavin-Python15042023\_PythonAdvanced\days.txt'
myFile = open(path,'r')
# print(myFile.read())    # try commenting this
# print(myFile.readline())
print(myFile.readlines()) # return a list of all the lines
        #   Note: readlines
        #       if we specify the parameter, the 
        #   lines exceeding the no of bytes from the hint
        #   parameter will not be returned by the 
        #   readlines method.

myFile.close()