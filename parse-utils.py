def remove_comments(file_to_remove):
    f=open(file_to_remove, 'r')
    file_to_write_to="junk/junk_output.txt"
    f2=open(file_to_write_to, 'a')
    onComment=False
    commentToRemove=""
    for line in f.readlines():
        for char in line:
            if char=="#":
                onComment=True
            elif char=="\n":
                onComment=False
                line.replace(commentToRemove, "")
            else:
                if onComment==False:
                    commentToRemove+=char
        f2.write(commentToRemove)

def main():
    remove_comments("./junk/testData.txt")

main()