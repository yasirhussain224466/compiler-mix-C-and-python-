
from wordbreak import wordBreak, is_keyword, is_punctuator, is_operator, is_identifier, is_int, is_float, is_char, is_str

class Token:
    cp = ''
    vp = ''
    line = 0


def lexicalAnalyzer():
    lineNo = 0
    com = False
    tokenSet = []
    with open("final.txt", "r") as inputFile:
        for line in inputFile:
            ##print(line)
            lineNo += 1
            temp, com = wordBreak(line, com)
           ## print(temp, com)

            if(not(com)):

                for word in temp:
                    if word != "":
                        newToken = Token()
                        if word[0].isdigit() or (word[0] == '.' and len(word) >= 2 and word[1].isdigit()):
                            if is_float(word):
                                newToken.cp = 'float_con'
                            elif is_int(word):
                                newToken.cp = 'int_con'
                            else:
                                newToken.cp = 'Invalid'
                        elif word[0].isalpha() or word[0] == "_":
                            if is_identifier(word):
                                k = is_keyword(word)
                                if k:
                                    newToken.cp = k
                                else:
                                    newToken.cp = 'id'
                            else:
                                newToken.cp = 'Invalid'
                        elif word[0] == "\"":
                            if is_str(word):
                                newToken.cp = 'str_con'
                            else:
                                newToken.cp = 'Invalid'
                        elif word[0] == "\'":
                            if is_char(word):
                                newToken.cp = 'char_con'

                            else:
                                newToken.cp = 'Invalid'
                        else:
                            oper = is_operator(word)
                            if oper:
                                newToken.cp = oper
                            elif is_punctuator(word):
                                newToken.cp = word
                            else:
                                newToken.cp = 'Invalid'

                        newToken.vp = word
                        newToken.line = lineNo
                        tokenSet.append(newToken)

    newToken = Token()
    newToken.cp = '$'
    newToken.vp = '$'
    newToken.line = lineNo
    tokenSet.append(newToken)
    return tokenSet

