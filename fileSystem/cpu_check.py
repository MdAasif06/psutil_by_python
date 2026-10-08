cpu=float(input("Enter the cpu"))

if cpu > 50:
    print("CPU over load")
elif cpu >20 and cpu < 50:
    print("send alert")
else:
    print("cpu normal")