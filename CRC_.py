iput_file="file.txt"

"""
Abdulrahman Ashraf
"""
def generator():
##    message,G,messageLen,divisorLen , poly = parser()
    global input_file
    try:
        with open(input_file, "r") as ins:
            arr = []
            arr = ins.read().splitlines()
        ins.close()
    except:
        print("wrong input file name")
    message=int(arr[0],2)
    G=int(arr[1],2)
    K=lonDev(message,G,len(arr[0]),len(arr[1]))
    F=message|K
    with open('generator.txt', 'w') as the_file:
        the_file.write("{0:b}".format(F))
        the_file.write('\n')
        the_file.write(arr[1])
    the_file.close()
##    print(F)
    return F

"""
Fouad 
"""
def generator():
    return

"""
Abdulrahman Ahmed 
"""
def verifier():
    return

def parser():
    return

"""
Miechel 
"""
def alter(index):
    return
    




