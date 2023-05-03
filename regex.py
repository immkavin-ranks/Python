    #   Regular Expressions
import re
string = 'Hello, my name is Kavin'
print(re.findall(r'Kavin', string))

string1 = 'Hello I live on lane 8 which is near street 42'
print(re.findall(r'\d', string1))
    # using modifiers 
    # >>>
print(re.findall(r'\d+', string1))

    # r  -> raw string literal
    # +  -> modifier
    # \d -> identifier

if re.search('awesome', "Isn't this an awesome view?"):
             print('You are awesome!')

result = re.split(r's', 'Awesome')
print(result)