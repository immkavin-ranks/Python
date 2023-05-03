path = r'Kavin-Python15042023\_PythonAdvanced\read.txt'

#       error is caused because the backslashes  \  in 
#  the file path are causing a problem with the argument
#  passed to  open() , as some of the characters 
#  following the backslash have a special meaning
#  in Python, and cause it to interpret the 
#  following characters in unintended ways. 
#       To fix this, you can either replace all 
#  backslashes  \  in the file path with forward
#  slashes  / , or you can use raw strings by 
#  prefixing the string literal with the letter  r .

OFile = open(path,'r')
# data = OFile.readline()
# print(data)

list = OFile.readlines(20)
print(list)
OFile.close()