iput_file="file.txt"

"""
Abdulrahman Ashraf
"""

"""
Fouad 
"""
def generator():
    global input_file
    try:
        i_file=open(input_file, "r")
        our_input = i_file.read().splitlines()
        i_file.close()
    except:
        print("please enter a correct file name")
    message=int(our_input[0],2)
    devisor=int(our_input[1],2)
    G=int(our_input[1],2)
    messageLen=len(our_input[0])
    divisorLen=len(our_input[1])
    R=lonDev(message,devisor,messageLen,divisorLen)
    frame=message|R
    gen_file=open('generator.txt', 'w')
    gen_file.write("{0:b}".format(frame))
    gen_file.write('\n')
    gen_file.write(our_input[1])
    gen_file.close()
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
    




