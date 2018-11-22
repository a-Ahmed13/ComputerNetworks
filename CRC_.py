iput_file="file.txt"

"""
Abdulrahman Ashraf
"""
def lonDev(message,devisor,messageLen,divisorLen):
    R=message>>(messageLen-divisorLen)
    i=messageLen-divisorLen
    R=devisor^R
    while 1 :
        i-=1
        if (1<<divisorLen-1)&R:
            R=R^devisor
        R=R<<1
        R|=((1<<i)&message)>>i
        if i==0:
            if(1<<divisorLen-1)&R:
                 R=R^devisor
            break
##    print(bin(R))
    return R

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
Abdelrahman Ahmed 
"""
def verifier():
     with open("generator.txt", "r") as ins:
        arr = []
        arr = ins.read().splitlines()
     ins.close()
     ins.close()
     message=int(arr[0],2)
     G=int(arr[1],2)
     K=lonDev(message,G,len(arr[0]),len(arr[1]))
     if K==0:
        print("the message is correct.\n______________________________________________")
     else:
        print("\nerror message.\n____________________________________________")
     return 

def parser():
    return

"""
Miechel 
"""
def alter(index):
    with open("generator.txt", "r") as ins:
        arr = []
        arr = ins.read().splitlines()
    ins.close()
    message=int(arr[0],2)
    index=len(arr[0])-index
##    print(arr[0])
    message^=(1<<index)
##    print(len(arr[0]))
    with open('generator.txt', 'w') as the_file:
        the_file.write("{0:b}".format(message))
        the_file.write('\n')
        the_file.write(arr[1])
    the_file.close()
##    print(bin(message))
    return message

"""
Miechel 
control
"""
print("Hello CRC :)\n============================================")
while 1:
    print("please enter  the input file name")
    input_file=input()
    print("\nfor generator->verifier please enter 1\nfor generator->alter->verifier please enter 2")
    des=input()
    if des == "1" :
        generator()
        verifier()
    elif des == "2" :
        index=input("please enter alter index\n")
        generator()
        alter(int(index))
        verifier()
    else :
        print("wrong input pleas try again")



