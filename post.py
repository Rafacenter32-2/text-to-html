conf = (open("config.conf")).read()
title = False
sep = False
exec(conf)
inpt = (open("input.txt"))
x = inpt.read()
if (title):
    y = input("titulo:")
    print ("okay")
x = x.replace("\n","<br>")
if (title):
    out = "<h1>"+ y +"</h1> <p>"+ x +"</p>"
else:
    out = "<p>"+ x +"</p>"
w = open("output.txt", "w")
w.write(out)
print("Pronto")
