import sys

f = open(sys.argv[1])
f1 = open(sys.argv[1] + ".new","w+")
buf = f.read()
bufnew = buf.replace("}","}\n")
bufnew = bufnew.replace(";",";\n")
f1.write(bufnew)
f.close()
f1.close()
