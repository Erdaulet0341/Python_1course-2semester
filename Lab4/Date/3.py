from datetime import datetime
now = datetime.now()
print("At the moment: ", end = "")
print(now.strftime("%d:%m:%Y %H:%M:%S:%f"))
print("Microseconds = ", end  ="")
print(now.strftime("%f"))