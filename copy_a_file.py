source_file = open("pic.png","rb")
target_file = open("output.png","wb")

data = source_file.read()
target_file.write(data)

source_file.close()
target_file.close()