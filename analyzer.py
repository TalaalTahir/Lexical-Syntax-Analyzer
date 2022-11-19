import re
class lexeme_anaylzer(object):
  
  with open('Lexical_Analyzer_Results.txt', 'w') as file:
    file.write("Lexical Analyzer Results: \n")
  file.close()

  def __init__(self,code):
    self.code = code
  
  def generateToken(self):
    
    code = self.code.split()
    current = 0
    tokens =[]
    while current < len(code):
      char = code[current]
      if char == "B": 
        addToken(char," --> BEGIN : 20")
        tokens.append(char)
    
      elif char == "E":
        addToken(char,"--> END: 21")
        tokens.append(char)
      elif char == "+":
        addToken(char,"--> ADD_OP: 1")
        tokens.append(char)
      elif char == "-":
        addToken(char,"--> SUB_OP: 2")
        tokens.append(char)
      elif char == "*":
        addToken(char,"--> MULT_OP: 3")
        tokens.append(char)
      elif char == "/":
        addToken(char,"--> DIV_OP: 4")
        tokens.append(char)
      elif char == "%":
        addToken(char,"--> MOD_OP: 5")
        tokens.append(char)
      elif char == "<":
        addToken(char,"--> LESS_THAN: 6")
        tokens.append(char)
      elif char == ">":
        addToken(char,"--> GREATER_THAN: 7")
        tokens.append(char)
      elif char == "<=":
        addToken(char,"--> LESS_THAN_EQUAL: 8")
        tokens.append(char)
      elif char == ">=":
        addToken(char,"--> GREATER_THAN_EQUAL: 9")
        tokens.append(char)
      elif char == "==":
        addToken(char,"--> EQUAL_TO: 10")
        tokens.append(char)
      elif char == "!=":
        addToken(char,"--> NOT_EQUAL_TO: 11")
        tokens.append(char)
      elif char == "=":
        addToken(char,"--> ASS_OP: 27")
        tokens.append(char)
      elif char == "whenever":
        addToken(char,"--> WHENEVER_CODE: 16")
        tokens.append(char)
      elif char == "however":
        addToken(char,"--> HOWEVER_CODE: 17")
        tokens.append(char)
      elif char == "go":
        addToken(char,"--> GO_CODE: 18")
        tokens.append(char)
      elif char == "{":
        addToken(char,"--> LEFT_BRACK: 23")
        tokens.append(char)
      elif char == "}":
        addToken(char,"--> RIGHT_BRACK: 24")
        tokens.append(char)
      elif char == "(":
        addToken(char,"--> LEFT_PAREN: 25")
        tokens.append(char)
      elif char == ")":
        addToken(char,"--> RIGHT_PAREN: 26")
        tokens.append(char)
      elif re.match('[0-2]*[0-5]*[0-5]*_[1]',char):
        addToken(char,"--> ONE_BYTE: 12")
        tokens.append(char)
      elif re.match('[0-3]*[0-2]*[0-7]*[0-6]*[0-9]*_[2]',char):
        addToken(char,"--> TWO_BYTES: 13")
        tokens.append(char)
      elif re.match('[0-9]*_[4]',char):
        addToken(char,"--> FOUR_BYTES: 14")
        tokens.append(char)
      elif re.match('[0-9]*_[8]',char):
        addToken(char,"--> EIGHT_BYTES: 15")
        tokens.append(char)
      elif re.match('^[\$Aa-zZ]{6,8}$',char):
        addToken(char,"--> VAL_NAME: 19")
        tokens.append(char)
      elif re.match('[n][u][m]',char):
        addToken(char,"--> ID: 0")
        tokens.append(char)
      else:
        print("Lexical Error, unknown lexeme")
        
      current += 1
    print("Lexical Anayzer finished!")
    return tokens

def addToken(char, str):
  with open('Lexical_Analyzer_Results.txt', 'a+') as file:
    file.write("Lexeme: " + char + ",Token "+ str +"\n")
  file.close()
    