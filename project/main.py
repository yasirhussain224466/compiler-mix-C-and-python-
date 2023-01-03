from lexical import lexicalAnalyzer
from syntax import SyntaxAnalyzer


if __name__ == "__main__":
    ts = lexicalAnalyzer()
    with open("tokens.txt", "w") as tokenFile:
            for t in ts:
                tokenFile.write(f"{t.cp}, {t.vp},  {t.line}\n")

    sa = SyntaxAnalyzer(ts)