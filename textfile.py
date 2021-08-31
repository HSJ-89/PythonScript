f = open("D:\HSJ\demofile2.txt", "a")
f.write("Now the file has more content!\n")
f.close()

#open and read the file after the appending:
f = open("D:\HSJ\demofile2.txt", "r")
print(f.read())

f = open("D:\HSJ\demofile2.txt", "w")
f.write("Deleted old!\n")
f.close()