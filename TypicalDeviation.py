import math
print "Enter all the numbers separated by comma(,):"
string_input = raw_input()
input_list = string_input.split(",")
input_list = [int(a) for a in input_list]
if (len(input_list)>4):
    for i in range(2):
        input_list.remove(max(input_list))
        input_list.remove(min(input_list))
    summary2=0
    for i in range(len(input_list)):
        summary2=(summary2+(input_list[i]-sum(input_list))**2)
    td=summary2/(len(input_list))*1.0
    print math.sqrt(td)
else:
    print "list is too sort"
