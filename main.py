from sys import argv

# Two parameters passed in
filePath = argv[1]
completionLevel = argv[2]

# 32 keywords for C language
keywords = ["auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else", "enum", "extern",
            "float", "for", "goto", "if", "int", "long", "register", "return", "short", "signed", "sizeof", "static",
            "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"]
keywordNum = 0

# Basic requirement implement
if completionLevel == "1":
    with open(filePath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("(", " ")
            line = line.replace(")", " ")
            line = line.replace(";", " ")
            line = line.replace("{", " ")
            line = line.replace("}", " ")
            line = line.replace(":", " ")
            words = line.split()
            for word in words:
                if word in keywords:
                    keywordNum += 1
    print("total num: ", keywordNum)
