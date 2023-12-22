def main(input):
    lines = input.splitlines()
    total1 = 0
    total2 = 0
    for line in lines:
        digits = [char for char in line if char.isnumeric()] #only add the char if its numeric, list comprehension yum
        if digits:
            total1 += int(digits[0] + digits[-1]) #first and last in each digits list
        digits = [char for char in translate(line) if char.isnumeric()]
        total2 += int(digits[0] + digits[-1])
        
    
    return total1,total2

def translate(line):
    for num, name in enumerate(digit_names):
        print (num,name)

digit_names = ["one","two","three","four","five","six","seven","eight","nine"]
main(open("test1.txt","r").read())