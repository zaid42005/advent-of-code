def main(input):
    lines = input.splitlines()
    total1 = 0
    for line in lines:
        print(line)
        digits = [char for char in line if char.isnumeric()] #only add the char if its numeric, list comprehension yum
        print (digits)
        total1 += int(digits[0] + digits[-1]) #first and last in each digits list
        print (total1)
    
    return 

main(open("test1.txt","r").read())