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

# Advanced  requirement implement
with open(filePath, 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace("(", " ").replace(")", " ").replace("{", " ") \
            .replace("}", " ").replace(";", " ").replace(":", " ")
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
    print("Coming soon")
elif completionLevel == "4":
    print("Coming soon")
else:
    print("Input the completion level between 1~4")
