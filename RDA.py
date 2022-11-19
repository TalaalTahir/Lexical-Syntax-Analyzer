import re
# <program> → ‘B’ <stmt> ‘E’
# <stmt> → <whenever_stmt> | <go_stmt> | <dec> | <block> | <ass>
# <block> → ‘{‘ { <stmt>   } ‘}’
# <whenever_stmt> →  ‘whenever’‘(‘<bool_expr>‘)’ <stmt> [ ‘however’ <stmt> ]
# <go_stmt> →  ‘go’‘(‘<bool_expr>‘)’ <stmt> 
# <dec> → 'num' 'id' 
# <ass> → ‘id’ ‘=’ <expr>
# <bool_expr> → <brel> { ( ‘!=’ | ‘==’ ) <brel>} 
# <brel> → <term> { ( ‘<=’ | ‘>=’ | ‘<’ | ‘>’ ) <term>} 
# <term> →  <expr> { ( ‘*’ | ‘/’ | ‘%’) <expr>}
# <expr> → <factor> { ( ‘+’ | ‘-’ ) <factor>} 
# <factor> → ‘id’ | ‘1_byte’ | ‘2_byte’ | ‘4_byte’ | ‘8_byte’ | ‘(‘ <term> ‘)’

class syntax_analyzer(object):

  def __init__(self, tokens):
    self.tokens = tokens
    self.current = 0
    self.currentToken = tokens[self.current]

  def getNextToken(self):
    if self.current < len(self.tokens):
      self.current += 1
    self.currentToken = self.tokens[self.current]

  def program(self):# <program> → ‘Begin’ <stmt> ‘END’

    if self.currentToken == 'B':
      self.getNextToken()
      self.stmt()
      if self.currentToken == 'E':
        print("Syntax Anyalizer finished")
        print("Your code is correct!")
      else:
        self.error()
    else:
      self.error()
    
  def stmt(self): # <stmt> → <whenever_stmt> | <go_stmt> | <ass> | <dec> | <block>
    if self.currentToken == 'whenever':
      self.whenever_stmt()
    elif re.match('[g][o]$',self.currentToken):
      self.go_stmt()
    elif re.match('^[\$Aa-zZ]{6,8}$',self.currentToken): 
      self.ass()
    elif re.match('[n][u][m]',self.currentToken):
      self.dec()
    elif self.currentToken == '{':
      self.block()
    else:
      self.error()
    
  def block(self): # <block> → ‘{‘ { <stmt> } ‘}’
    if self.currentToken == '{':
      self.getNextToken()
      while self.currentToken == 'whenever' or self.currentToken == "go" or re.match('[n][u][m]',self.currentToken) or self.currentToken == '(' or re.match('^[\$Aa-zZ]{6,8}$',self.currentToken):
        self.stmt()
      if self.currentToken == '}':
        self.getNextToken()
      else:
        self.error()
    else:
      self.error()
      
  def whenever_stmt(self): # <whenever_stmt> →  ‘whenever’‘(‘<bool_expr>‘)’ <stmt> [ ‘however’ <stmt> ]
    if self.currentToken == 'whenever':
      self.getNextToken()
      if self.currentToken == '(':
        self.getNextToken()
        self.bool_expr()
        if self.currentToken == ')':
          self.getNextToken()
          self.stmt()
          if self.currentToken == 'however':
            self.getNextToken()
            self.stmt()
          else:
            self.error()
        else:
          self.error()
      else:
        self.error()
    else:
      self.error()
      
  def go_stmt(self): # <go_stmt> →  ‘go’‘(‘<bool_expr>‘)’ <stmt> 
    if self.currentToken == 'go':
      self.getNextToken()
      if self.currentToken == '(':
        self.getNextToken()
        self.bool_expr()
        if self.currentToken == ')':
          self.getNextToken()
          self.stmt()
        else:
          self.error()
      else:
        self.erorr()
    else:
      self.error()
  def dec(self): # <dec> → 'num' 'id' 
    if re.match('[n][u][m]',self.currentToken):
      self.getNextToken()
      if re.match('^[\$Aa-zZ]{6,8}$',self.currentToken):
        self.getNextToken()
        self.ass()
      else:
        self.error()
    else:
      self.error()

  def ass(self): # <ass> → ‘id’ ‘=’ <expr> 
    if re.match('^[\$Aa-zZ]{6,8}$',self.currentToken):
      self.getNextToken()
      if self.currentToken == '=':
        self.getNextToken()
        self.term()
      else:
        self.error()
    else:
      self.error()
  def bool_expr(self): # <bool_expr> → <brel> { ( ‘!=’ | ‘==’ ) <brel>} 
    self.brel()
    while self.currentToken == '!=' or self.currentToken == '==':
      self.getNextToken()
      self.brel()
      
  def brel(self): # <brel> → <term> { ( ‘<=’ | ‘>=’ | ‘<’ | ‘>’ ) <term>} 
    self.term()
    while self.currentToken == '<=' or self.currentToken == '>=' or self.currentToken == '<' or self.currentToken == '>' :
      self.getNextToken()
      self.term()
      
  
  def term(self): # <term> →  <expr> { ( ‘*’ | ‘/’ | ‘%’) <expr>}
    self.expr()
    while self.currentToken == '*' or self.currentToken == '/' or self.currentToken == '%':
      self.getNextToken()
      self.expr()
      
  def expr(self):
     # <expr> → <factor> { ( ‘+’ | ‘-’ ) <>} 
    self.factor()
    while self.currentToken == '+' or self.currentToken == '-':
      self.getNextToken()
      self.factor()
  
  def factor(self):
    #<factor> → ‘id’ | ‘1_byte’ | ‘2_byte’ | ‘4_byte’ | ‘8_byte’ | ‘(‘ <term> ‘)’
    if re.match('^[\$Aa-zZ]{6,8}$',self.currentToken) or re.match('[0-2]*[0-5]*[0-5]*_[1]',self.currentToken) or re.match('[0-9]*_[4]',self.currentToken) or re.match('[0-3]*[0-2]*[0-7]*[0-6]*[0-9]*_[2]',self.currentToken) or re.match('[0-9]*_[8]',self.currentToken):
      self.getNextToken()
    elif self.currentToken == '(':
      self.getNextToken
      self.term()
      if self.currentToken == ')':
        self.getNextToken()
      else:
        self.error()
    else:
      self.error()
  
  def error(self):
    print("Syntax Error Code terminated")
    raise SystemExit