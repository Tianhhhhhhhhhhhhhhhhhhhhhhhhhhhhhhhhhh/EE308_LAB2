# EE308_LAB2
 Extract keywords of different levels from the C or C++ code files that are read in

| **The Link Your Class**                    | [EE308 MIEC社区-EE308 MIEC论坛-CSDN社区云](https://bbs.csdn.net/forums/MUEE308FZ) |
| ------------------------------------------ | ------------------------------------------------------------ |
| The Link of Requirement of This Assignment | [LAB 2 Individual programing work (EE308 IEC MU 2021 Fall)-CSDN社区](https://bbs.csdn.net/topics/600798588) |
| The Aim of This Assignment                 | Extract keywords from the C code files                       |
| MU STU ID and FZU STU ID                   | 19105266_83190137                                            |

#### **Github Repository Address**

[EE308_LAB2 (github.com)](https://github.com/Tianhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh/EE308_LAB2)

## 1. PSP Form

| PSP                                     | Time Estimated (min) | Time Spent (min) |
| --------------------------------------- | -------------------- | ---------------- |
| **Planning**                            | -                    | -                |
| · Estimate                              | 10                   | 10               |
| **Development**                         | -                    | -                |
| · Analysis                              | 40                   | 45               |
| · Design Spec                           | 0                    | 0                |
| · Design Review                         | 0                    | 0                |
| · Coding Standard                       | 0                    | 0                |
| · Design                                | 25                   | 25               |
| · Coding                                | 180                  | 180              |
| · Code Review                           | 90                   | 90               |
| · Test                                  | 30                   | 30               |
| **Reporting**                           | -                    | -                |
| · Test Report                           | 60                   | 60               |
| · Size Measurement                      | 20                   | 20               |
| · Postmortem & Process Improvement Plan | 20                   | 20               |
| **Summary**                             | 475                  | 480              |

## 2. Problem-solving Ideas

​	First, I should choose the language this work used. Because I know little about Java, so I exclude it at first. Then, this programing work is most about solve string, so I would prefer to use Python than C++ because of the convenient functions in Python.

​	In order to solve the problem, str.replace() and str.split() can help a lot. Then I only need to compare the order and position of those C keywords to distinguish switch-case, if-else and if-elseif-else.

## 3. Design and implementation process



## 4. Code description

```python
line = line.replace("(", " ( ").replace(")", " ) ").replace(";", " ; ").replace("{", " { ").replace("}", " } ").replace(":", " : ")
```

This code is to process punctuations in the lines read from C file.

```
if word == "switch":
    switchNum += 1
if word == "case":
    tempNum += 1
if word == "default":
    caseNum.append(tempNum)
    tempNum = 0
```

This code is used for counting switch number and the case number in switch. For convenience, I assumed each switch have a 'default'.

```
if word == "if":
    if preElse == 1:
        if preElseIf == 0:
            preElseIf = 1
            elseIfNum += 1
        preElse = 0
    else:
        preElseIf = 0
if preElse == 1:
    if elseIfNum != 0:
        ifElseifElseNum += 1
        elseIfNum -= 1
    else:
        ifElseNum += 1
    preElse = 0
if word == "else":
    preElse = 1
```

This code is used to distinguish 'if-else' and 'if-else if-else'. I assumed each 'if' have each. Thanks to the process of C file, this code can deal with unformed C codes.

## 5. Unit test

The difficulty of this work is to solve nested 'if-else' and unformed codes. So that I write some nested 'if-else' and unformed code to test my code. I have found some bugs through this method and fixed them.

And I do not know how to use some tools to do unit test and optimize it. So I try to use my brain to make this code better.

## 6. Summary

Because I already know how to use git (especially 'git clone' x_x), I do not need too much preparation for this programming work.

But we did not focus on testing codes before, so I am confused about how to do unit test and then optimize the code. I will then spend more time on this part later. And there still have some situations I cannot solve, I will fix them later.

And I find a more convenient method to do this is using *regular expression*. I will try it later.

