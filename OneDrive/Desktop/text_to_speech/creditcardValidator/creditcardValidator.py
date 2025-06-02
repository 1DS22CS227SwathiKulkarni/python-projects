card_no = "5610591081018250"

ls = []
sum_of_odd = 0
for i,val in enumerate(card_no):
    if i%2 != 0:
        #sum of numbers at odd index
        sum_of_odd = sum_of_odd + int(val)
    else:
        #numbers at even index connverted to list
        ls.append(int(val)*2)

double_string = ""

for x in ls:
    double_string += str(x)

even_ls = list(double_string)
#print(even_ls)

sum_of_even = 0

for i in even_ls:
    sum_of_even += int(i)

#print(sum_of_even)

sum = sum_of_even + sum_of_odd
if sum%10 == 0:
    print("Valid Card!")
else:
    print("Invalid Card :(")