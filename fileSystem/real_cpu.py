import psutil


threshold=float(input("Enter your threshold value"))
for i in range(5):
    if psutil.cpu_percent(interval=1) > threshold:
        print("CPU is unhealthy")
    else:
        print("CPU good condition")

# print(psutil.cpu_percent(interval=1))
# print(dir(psutil))
# print(psutil.cpu_times_percent())