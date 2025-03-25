def btd():
    num = str(input('enter your 8-bit binary sequence(type like this: 01010101)'))
    endval = 0
    multis = [128,64,32,16,8,4,2,1]
    number = [0,1,2,3,4,5,6,7]
    for item in number:
        match num[item - 1]:
            case "1":
                endval = endval + multis[item - 1]
            case "0":
                pass
    print(endval)
def dtb():
    num = int(input('enter your decimal number(type like this: 24). Note: The number has to be equal to or less than 255'))
    endval = []
    multis = [128,64,32,16,8,4,2,1]
    number = [0,1,2,3,4,5,6,7]
    for item in number:
        if num - multis[item] >= 0:
            num = num - multis[item]
            endval.append("1")
        elif num - multis[item] <= 0:
            endval.append("0")
    x = "".join(endval)
    print(x)
def main():
    funcrequest = input('Would you like to use binary to decimal(type: btd, has to be 8-bits) or decimal to binary(type: dtb, has to be under or equal to 255, and over and equal to 0)').upper()
    match funcrequest:
        case "BTD":
            btd()
        case "DTB":
            dtb()
