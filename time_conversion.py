def validate():
    loop = True
    while loop:
        try:
            time = input("\nPlease enter time in seconds: ")
            time = int(time)
            
            if time <= 0:
                print("\nPlease enter a number bigger than zero! ")
                loop = True
            else:
                loop = False
        except ValueError:
            print("\nPlease enter a whole number! ")
            loop = True
    return time

def convert(t):
    
    day = t // (24 * 3600)
 
    t = t % (24 * 3600)
    hour = t // 3600
 
    t %= 3600
    minutes = t // 60
 
    t %= 60
    seconds = t

    print("{} day(s), {} hour(s), {} minute(s), {} day(s)".format(day, hour, minutes, seconds))

    
def main():
    time = validate()
    convert(time)
    
main()
