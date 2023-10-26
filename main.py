import time
import random
class Cypher():
    global a
    a = input("What text do you want to cypher?\n")
    print("Cyphering...")
    time.sleep(2)
    print("Cyphered, here is your cypher code...")
    time.sleep(.5)
    print(random.randint(1, 9999999999))
class DeCypher():
    k = input("Enter cypher code to decypher or press ENTER to cancel...\n")
    if k == "":
        pass
    else:
        print("Decyphering...")
        time.sleep(2)
        print("Decyphered, here is the text...")
        time.sleep(.5)
        print(a)



