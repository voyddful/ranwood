def flip(num):
    numer = str(num)
    list = []
    count = 1
    length = len(str(num))
    i = length - 1
    while 0 <= i:
        expo = 10 ** i
        while num - expo >= expo:
            count = count + 1
            num = num - expo
        if count >= 10:
            count = count - 10
        list.append(count)
        count = 1  
        i = i - 1
    numm = 0
    text = ""
    lengthh = length
    while length > 0:
        length = length - 1
        text = text + str(list[length])
        numm = numm + list[length]
    if text == numer:
        print("your number is a pallindrome!!")
    else:
        print("your number is not a palindrome!!")   
    print(f"The summation of these numbers are: {numm}" )
def main():
    givennum = int(input("give me an integer, it has to be above 0: "))
    flip(givennum)
