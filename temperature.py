#!/usr/bin/env/python3
f=0
while f<=250:
    t=(f-32)/1.8
    print("{:5d} , {:7.2f}".format(f,t))
    f+=25
f=float(input("Please input a Fahrenheit:"))
t=(f-32)/1.8
print("Fahrenheit is {:7.2f},Celsius is {:7.2f}".format(f,t))

