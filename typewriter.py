import sys,time,os


def typewriter(message): #fonction name
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        
        if char != "\n":
            time.sleep(0.07) #spacing between each letter
        else:
            time.sleep(1) #spacing between each paragraph
            

os.system("cls") #clear