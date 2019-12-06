# Imports from the backend and frontend of Quinterac
import backend as backend
import front_end as front_end
from importlib import reload

# runs a daily session
def dailySession():
    #reset all variables in the front end file
    reload(front_end)
    #call front end's main function
    front_end.main()

    infile = open("tsf.txt", "r")
    lines = infile.read().splitlines()

    outfile = open("tsf.txt", "w")
    #fix format of the merged tsf file, removing duplicate EOS lines
    for i in lines:
        if (i != "EOS 0000000 000 0000000 ***"):
            outfile.write(i + "\n")
    outfile.write("EOS 0000000 000 0000000 ***")
    outfile.close()

    #call back end's main function
    backend.main()


# Driver main file
def main():
    # loop the daily driver code for 5 days
    for i in range(5):
        while(True):
            next = input("Press enter to continue to next day. \n")
            if (next == ''):
                print("Day " + str(i + 1))
                dailySession()
                break
            else:
                print('You typed some text before pressing enter.')

main()
