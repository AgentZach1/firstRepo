from asyncio.windows_events import NULL

#Read each line from 25-Jan-Filesystems.txt
#Put each line in an array
oldFile = open("./25-Jan-Filesystems.txt", 'r')
if (oldFile == NULL):
    print("Failed Read")
fLines = []
fLines = oldFile.readlines()
oldFile.close()

newFile = open('./textFile.txt', 'w')
if (newFile == NULL):
    print("Failed Creation")
i = 0
for line in fLines:
    if 'cd' in fLines[i]:
        newFile.write('====================\n')
        print('Line ' + str(i+1) + ': ====================')
    else:
        newFile.write(fLines[i])
        print('Line ' + str(i+1) + ': ' + fLines[i])
    i+=1
newFile.close()
