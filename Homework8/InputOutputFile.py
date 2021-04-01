import os
files= ['hello']
def fileHandling():
    while(True):
        FileName = input("Please enter the filename\n")
        if(FileName in files):
            ReadOption = input("Do you want to read\n")
            if(ReadOption == "yes"):
                print("read")
                ReadFile = open(FileName, "r+")
                read = ReadFile.read(20)
                print("Read : ", read)
                ReadFile.close()
                break
            else:
                DeleteOption = input("Do you want to delete the file and start over\n")
                if(DeleteOption == "yes"):
                    print('Delete')
                    DeleteFile = open(FileName,'w')
                    DeleteFile.close()
                    os.remove(FileName)
                    files.remove(FileName)
                    print(files)
                    break
                else:
                    AppendOption = input("Do you want to append the file\n")
                    if(AppendOption =="yes"):
                        print('Append the file')
                        AppendFile = open(FileName, "w")
                        AppendFile.write("Hello everyone\n")
                        AppendFile.close()
                        break
                    else:
                        print(files)
        else:
            file = open(FileName, "wb")
            file.close()
            print(file.closed)
            files.append(file.name)
        print(files)
