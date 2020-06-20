
memo_file = open('/Users/aimi/Desktop/memo.txt','r')
print(memo_file.readable())     # check if the file is readable
print(memo_file.read())         # display all the data

print(memo_file.readline())     # display the first line(repeat this line will go to the next line)
print(memo_file.readlines())    # display all the data as a list



memo_file.close()               # MAKE SURE CLOSE THE FILE!!!!
