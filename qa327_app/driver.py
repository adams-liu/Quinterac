# Imports from the backend and frontend of Quinterac
import backend as backend
import front_end as front_end

# runs a daily
def dailySession():
    front_end.main()

    infile = open("tsf.txt", "r+")
    lines = infile.read().splitlines()
    outfile = open("tsf.txt", "w")
    for i in lines:
        if (i != "EOS 0000000 000 0000000 ***"):
            outfile.write(i + "\n")
    outfile.write("EOS 0000000 000 0000000 ***")
    outfile.close()
    backend.main()

# Driver main file
def main():
 for i in range(5):
    print("Day " + str(i+1))
    dailySession()

main()
