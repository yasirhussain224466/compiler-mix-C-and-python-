import re
# Keywords
kw = {
    "dt": ["int", "float", "char", "boolean", "var"],
    "string": ["string"],
    "const": ["const"],
    "if": ["if"],
    "else": ["else"],
    "switch": ["switch"],
    "case": ["case"],
    "default": ["default"],
    "return": ["return"],
    "break": ["break"],
    "bool": ["true", "false"],
    "null": ["null"],
    "for": ["for"],
    "while": ["while"],
    "do": ["do"],
    "void": ["void"],
    "try": ["try"],
    "catch": ["catch"],
    "finally": ["finally"],
    "new": ["new"],
    "final": ["final"],
    "class": ["class"],
    "extend": ["extend"],
    "implement": ["implement"],
    "static": ["static"],

    "access-modifier": ["private", "public", "protected"],

}

# Punctuators
punctuator = [".", ",", ":", ";", "{", "}", "(", ")", "[", "]"]

# Operators
operators = {
    "incdec": ["++", "--"],
    "ro": ["<", ">", "<=", ">=", "!=", "=="],
    "**": ["**"],
    "mdm": ["*", "/", "%"],
    "pm": ["+", "-"],
    "and": ["and"],
    "or": ["or"],
    "not": ["not"],
    "=": ["="],
    "ra": ["+=", "-=", "*=", "/=", "%="]
}

# Identifier
idf = "^[A-Za-z_][A-Za-z0-9_]*$"

# Constant
int_con = "^[+-]?[0-9]+$"

float_con = "^[+-]?[0-9]*[.][0-9]+(e[+-]?[0-9]+)?$"
##float_con = "^[+-]?[0-9]*[.][0-9]?$"

s1 = "\\\\\"\'"
s2 = "0123456789cdeghijklmnpqsvwyzABCDEFGHIJKLMOPQRSTVWXYZ!#\$%&\(\)*+,-./:;<=>?@\[\]\^_`{|}~"
s3 = "nabfrtxoUuN"

char_con = f"^\'(([\\\\][nabfrtxoUuN\\\\])|([^\\\\]))\'$"
#char_con = f"^\'([\n][\\][{s1}{s3}]|[{s2}]|[{s3}])'$"
##char_con = f"^\'([\n][\\][{s1}{s3}]|[{s2}]|[{s3}])\'$"
#char_con = f"^\'(\[{s1}{s3}]|[{s2}]|[{s3}])'$"
str_con = f"^\"(.)*\"$"


# Function to check the given characher is a punctuator
def is_punctuator(ch):
    for p in punctuator:
        if p == ch:
            return True
    return False


# Function to check the given characher is an operator
def is_operator(ch):
    for o in operators:
        for a in operators[o]:
            if a == ch:
                return o
    return None


# Function to check the given characher is a keyword
def is_keyword(ch):
    for k in kw:
        for a in kw[k]:
            if a == ch:
                return k
    return None


# Function to check the given characher is an identifier
def is_identifier(ch):
    result = re.match(idf, ch)
    if result:
        return True
    else:
        return False


# Function to check the given characher is an integer constant
def is_int(ch):
    result = re.match(int_con, ch)
    if result:
        return True
    else:
        return False


# Function to check the given characher is an float constant
def is_float(ch):
    result = re.match(float_con, ch)
    if result:
        return True
    else:
        return False


# Function to check the given characher is an char constant
def is_char(ch):
    result = re.match(char_con, ch)
    if result:
        return True
    else:
        return False


# Function to check the given characher is an string constant
def is_str(ch):
    result = re.match(str_con, ch)
    if result:
        return True
    else:
        return False


# Wordbreak function
def wordBreak(line, com):

    index = 0
    temp = []
    tempStr = ""
    if com:
        tempStr = "##"
    while index < len(line):
        ch = line[index]

        if ch == "\"" and tempStr not in ["#", "##"]:
            if tempStr != '':
                temp.append(tempStr)
            tempStr = ch
            tempI = index + 1
            hasEscaped = False
            while(tempI < len(line)):
                ch = line[tempI]
                tempStr += ch

                if(ch == "\""):
                    break


                if(ch == "\\" ):
                    if(not hasEscaped and line[tempI + 1] == "\""):
                        tempStr += line[tempI + 1]
                        tempI += 1
                    elif(hasEscaped):
                        hasEscaped = False
                    else:
                        hasEscaped = True


                tempI += 1

            index = tempI
            temp.append(tempStr)
            tempStr = ''

        elif ch == "\'":
            if tempStr != '':
                temp.append(tempStr)
            tempStr = ch
            if ((index+1) < len(line) and line[index + 1] == "\\"):
                loopStop = 3
            else:
                loopStop = 2
            tempI = 1

            while((index + tempI) < len(line) and tempI<=loopStop):
                tempStr += line[index + tempI]
                tempI += 1


            index += loopStop + 1
            if(index < len(line)):
                temp.append(tempStr)
                tempStr = ''
            continue
        elif tempStr != "" and tempStr[0] == "\"":
            tempStr += ch

        elif tempStr == "##":
            if ch == "#":
                tempStr += ch
        elif tempStr == "###":
            if ch == "#":
                tempStr = ""
            else:
                tempStr = "##"
        elif tempStr == "#":
            if ch == "#":
                tempStr += ch
            else:
                com = True
                tempStr = ''
            break
        elif ch == '#':
            tempStr = ch
        elif ch == "\n":
            if tempStr != "\'":
                temp.append(tempStr)
                tempStr = ""
            else:
                tempStr += ch
        elif ch == " ":
            if tempStr != "":
                temp.append(tempStr)
            tempStr = ""
        elif is_punctuator(ch) == True:
            if ch == "." and (tempStr.isdigit() or tempStr == ""):
                tempStr += ch
            elif tempStr != "":
                temp.append(tempStr)

                tempStr = ch
            else:
                temp.append(ch)
        elif tempStr != "" and (ch == '+' or ch == '-') and tempStr[len(tempStr) - 1] == "e":
            tempStr += ch
        elif is_operator(ch) != None:
            append = False
            if tempStr != "":
                if tempStr == '+' and (ch == '+' or ch == '='):
                    append = True
                    tempStr += ch
                elif tempStr == '-' and (ch == '-' or ch == '='):
                    append = True
                    tempStr += ch
                elif tempStr == '*' and (ch == '*' or ch == '='):
                    append = True
                    tempStr += ch
                elif tempStr == '/' and ch == '=':
                    append = True
                    tempStr += ch
                elif tempStr == '%' and ch == '=':
                    append = True
                    tempStr += ch
                elif tempStr == '>' and ch == '=':
                    append = True
                    tempStr += ch
                elif tempStr == '<' and ch == '=':
                    append = True
                    tempStr += ch
                elif tempStr == '=' and ch == '=':
                    append = True
                    tempStr += ch
                elif tempStr == '!' and ch == '=':
                    append = True
                    tempStr += ch
                temp.append(tempStr)
                tempStr = ""
            if not append:
                tempStr = ch

        elif is_int(ch) and tempStr == ".":
            tempStr += ch
        else:
            if is_operator(tempStr) != None or is_punctuator(tempStr) == True:
                temp.append(tempStr)
                tempStr = ''

            tempStr += ch

        index += 1
    else:
        if tempStr not in ["\n", '', "#", "##"]:
            temp.append(tempStr)

    com = False
    if tempStr == "##":
        com = True

    return temp, com
