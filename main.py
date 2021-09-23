from sys import argv

# Two parameters passed in
filePath = argv[1]
completionLevel = argv[2]

# 32 keywords for C language
keywords = ["auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else", "enum", "extern",
            "float", "for", "goto", "if", "int", "long", "register", "return", "short", "signed", "sizeof", "static",
            "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"]

keywordNum = 0
switchNum = 0
caseNum = []
tempNum = 0
ifElseNum = 0
ifElseifElseNum = 0
preElse = 0
preElseIf = 0

# Ultimate requirement implement
with open(filePath, 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace("(", " ( ").replace(")", " ) ").replace(";", " ; ") \
            .replace("{", " { ").replace("}", " } ").replace(":", " : ")
        words = line.split()
        for word in words:
            # count keywords
            if word in keywords:
                keywordNum += 1

            # count switch and case
            if word == "switch":
                switchNum += 1
            if word == "case":
                tempNum += 1
            if word == "default":
                caseNum.append(tempNum)
                tempNum = 0

            # count if-else and if-elseif-else
            if word == "if":
                if preElse == 1:
                    preElseIf += 1
                    preElse = 0
            if preElse == 1:
                if preElseIf != 0:
                    ifElseifElseNum += 1
                    preElseIf -= 1
                else:
                    ifElseNum += 1
                preElse = 0
            if word == "else":
                preElse = 1

# Output
if completionLevel == "1":
    print("total num:", keywordNum)
elif completionLevel == "2":
    print("total num:", keywordNum)
    print("switch num:", switchNum)
    output = ""
    for i in caseNum:
        output += str(i) + " "
    print("case num:", output)
elif completionLevel == "3":
    print("total num:", keywordNum)
    print("switch num:", switchNum)
    output = ""
    for i in caseNum:
        output += str(i) + " "
    print("case num:", output)
    print("if-else num:", ifElseNum)
elif completionLevel == "4":
    print("total num:", keywordNum)
    print("switch num:", switchNum)
    output = ""
    for i in caseNum:
        output += str(i) + " "
    print("case num:", output)
    print("if-else num:", ifElseNum)
    print("if-elseif-else num:", ifElseifElseNum)
else:
    print("Input the completion level between 1~4")
