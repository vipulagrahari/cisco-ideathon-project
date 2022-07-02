# VIP - 2022 Industry Problerm Statement 

#name - vipul agrahari
#college - Shri Ram Institute of Technology, Jabalpur
#Roll number - 0205CS191121




import sys


def main(numAdds):


    # task 1 - Ask the user for 10 inputs, these 10 inputs are ipv4 addresses. 
    
    inputAddresses = []
    
    
    print("Please Enter 10 IPv4 Addresses.")
    
    for i in range(numAdds):
        inputAddresses.append(input())

    # task 2 and task 3 - Check if the addresses are valid and add them to a list.

    result = []

    for address in inputAddresses:
        
        if checkIP(address):
            result.append(address + ", " + getOthers(address))
        else:
            result.append("Invalid")


    with open("out.txt", "w") as file:
        for i in range(numAdds):
            file.write(f"{result[i]}\n")
        

    # for i in range(len(result)):
    #     print(f"The {num[i]} IP address in Decimal, Binary, Octal and Hexadecimal format is ")       
    return result

    


def checkIP(address):

    flag = False
    subAdds = address.split(".")

    if len(subAdds) != 4 :
        return flag
    

    for x in subAdds:
        
        if int(x) <= 255 and int(x) >= 0: 
            if len(x) > 1 and x[0] != "0":
                flag = False
            else:
                flag = True
    
    return flag


def getOthers(address):

    subAdds = [int(x) for x in address.split(".")]

    binary = []
    octal = []
    hexadecimal = []
    

    for x in subAdds:
        binary.append( bin(x).replace("0b", "") ) 
        octal.append( oct(x).replace("0o", "") )
        hexadecimal.append( hex(x).replace("0x", ""))
    
    
    return ".".join(binary) + ", " + ".".join(octal) + ", " + ".".join(hexadecimal)


if __name__ == "__main__":

    num = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eight", "ninth", "tenth"]
    numAdds = 10
    result = main(numAdds)
    
    for i in range(numAdds):
        print(f"The {num[i]} IP address in Decimal, Binary, Octal and Hexadecimal format is {result[i]}")
