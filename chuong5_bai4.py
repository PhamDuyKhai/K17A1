
a=float(input("giá trị cạnh thứ nhất"))
b=float(input("giá trị cạnh thứ hai"))
c=float(input("giá trị cạnh thứ ba"))
q=(a+b+c)/2
import math
s=math.sqrt(q*(q-a)*(q-b)*(q-c))
print("diện tích tam giác =",s)

