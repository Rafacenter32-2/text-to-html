inpt = (open("input.txt"))
x = inpt.read()
y = input("titulo:")
x = x.replace("\n","<br>")
out = "<h1>"+ y +"</h1> <p>"+ x +"</p>"
w = open("output.txt", "w")
w.write(out)
