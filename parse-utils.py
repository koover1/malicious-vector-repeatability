def remove_comments(file_to_remove):
    f=open(file_to_remove, 'r')
    file_to_write_to="junk/junk_output.txt"
    f2=open(file_to_write_to, 'w')
    onComment=False
    stringToAdd=""
    for line in f.readlines():
        for index, char in enumerate(line):
       #     print(char)
            if char=="#" and onComment==False:
                onComment=True
            elif char=="n" and line[index-1]=="\\" and onComment==True:
                print("done with comment")
                onComment=False
            else:
                if onComment==False:
                    stringToAdd+=char
        stringToAdd=stringToAdd+"\n"
        f2.write(stringToAdd)

def main():
    remove_comments("./junk/testData.txt")

main()