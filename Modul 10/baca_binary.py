f = open ("bfile.img", "wb+")
message = "Hello kamu"
encode = message.encode("utf-16")
f.write(encode)
f.seek(0)
bdata = f.read()
print ("Binary data : ", bdata)
decode = bdata.decode("utf-16")
print ("Normal data : ", decode)
