path = r'Kavin-Python15042023\_PythonAdvanced\read.txt'
OFile = open(path, 'a')
OFile.write("I'm Kavin.")
OFile = open(path, 'r')
content = OFile.read()
print(content)

OFile.close()