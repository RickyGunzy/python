
def celcius_to_farenheit():
    temp = input("\nPlease enter temperature in Celcius: ")
    org = temp
    temp = (float(temp) * 9/5) + 32
    print(org + '\u00b0C = ' + "{:.2f}".format(temp) + '\u00b0F')

def farenheit_to_celcius():
    temp = input("\nPlease enter temperature in Farenheit: ")
    org = temp
    temp = (float(temp) - 32) * 5/9
    print(org + '\u00b0F = ' + "{:.2f}".format(temp) + '\u00b0C')
    
again = True

while again:
    choice = input("\n\t Press and enter... \n"
             +"'F' to convert Farenheit to Celcius \n"
             + "'C' to convert Celcius to Farenheit \n"
             + "'X' to exit \n"
             +"Choice: ")

    if choice == 'C' or choice == 'c':
        celcius_to_farenheit()
        again = True

    elif choice == 'F' or choice == 'f':
        farenheit_to_celcius()
        again = True
        
    elif choice == 'X' or choice == 'x':
        again =False
        
    else:
        print("\nInvalid input! Please try again.\n")
        again = True
