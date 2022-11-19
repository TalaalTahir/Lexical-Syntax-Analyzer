import lexical
import RDA

def main():
  input_string = input("Enter input file ending in .txt: ")
  input_file = open(input_string, "r")
  if input_file == None:
    print("file does not exist")
  else:
    with open(input_string, "r") as input_file:
      text = input_file.read()
  analyze = lexical.lexeme_anaylzer(text)
  tokens = analyze.generateToken()
  syntax = RDA.syntax_analyzer(tokens)
  objs = syntax.program()
  input_file.close()
main()
