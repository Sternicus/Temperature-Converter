import time,os,sys

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.13)
  
typingPrint ("This is a Temperature Converter"'\n')
print ("_______________________________"'\n')
farenheit = int(input('Enter your number in Farenheit: '))
convertf = (farenheit - 32) * 0.5556
convertk = convertf + 273.15
convertr = farenheit + 459.67
convertren = (farenheit -32)*0.44444
    
print("Here is your number in Celsius:",convertf)
print("Here is your number in Kelvin:", convertk)
print("Here is your number in Rankine:",convertr)
print("Here is your number in Reaumur:",convertren)
