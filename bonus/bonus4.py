filenames = ["1.Raw Data.txt", "2.Reports.txt","3.Presentations.txt"]
#strings are immutable(cannot be changed)
#lists are immutable
for filename in filenames:
    filename = filename.replace('.','-',1)
    print(filename)
#to ma a mutable list you can use a tuple
#example: filenames = ("1.Raw Data.txt", "2.Reports.txt","3.Presentations.txt")
