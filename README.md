# Lexical-Syntax-Analyzer
This was part of a project for my CSC 4330 class. I have created a lexical and syntax analyzer for a programming language that I will be creating. I have used parts of different languages such as Java and C to create my own language. Included in this repository is the lexical analyzer labeled lexical.py, syntax analyzer labeled RDA.py, and test files labeled as Correct1.txt, Correct2.txt, Lexical_Errors.txt, and Syntax_Errors.txt. 

-Parts E, F, G: The analyzers and test files.

To run the lexical and syntax analyzer download the code and open main.py. Then run the code on your ide of choice. The program will ask you to input a file. I have included 4 test files: Correct1.txt, Correct2.txt, Lexical_Errors.txt, and Syntax_Errors.txt. The user has the choice of choosing out of these files or making their own file to check if it follows the rules of my language. Correct1.txt & Correct2.txt will run perfectly and produce a message saying they are both written properly. Lexical_Errors.txt & Syntax_Errors.txt will produce errors that the user can look through, for these two files to run the user can delete the commented lines as indicated in the files or not, if the commented lines are not deleted the program will produce more lexical error messages. The program will also produce a file called Lexical Analyzer Results which will have each lexeme its Toke code and what Token it is. The user can go in the code and change the returning file name. 

-Part A:
The Token Codes for the lexeme are as follows.

![image](https://user-images.githubusercontent.com/77017392/202861256-5b1ca24e-021e-4b4c-9804-800ad61131ae.png)

The rules for the lexme are as follows.

![image](https://user-images.githubusercontent.com/77017392/202861790-9f0e1599-0d91-40f0-9c52-9e4ddfda9b91.png)

-Part B: 
The production rules for my languge are as follows:

![image](https://user-images.githubusercontent.com/77017392/202862077-5e3005ee-fdb7-4db7-bf5d-c52e5d0d58a6.png)

-Parts C & D:
The Pairwise disjoini test

![image](https://user-images.githubusercontent.com/77017392/202862156-11e315e1-707b-4794-a757-e42882ffcc76.png)

The Pairwise disjoint test is passed and there is no left recursion, meaning this conforms to the standard of an LL Grammar. There are no two ways to get the same string meaning the grammar is not ambiguous, passing the test for ambiguous grammar also. 

Part H:

Below is the basic LR(1) table for arithmetic. 

![image](https://user-images.githubusercontent.com/77017392/202866809-58a328f8-27e0-458d-8b12-84a7f5f8b5a6.png)

Tracing code for 1 correct sample would be:

![image](https://user-images.githubusercontent.com/77017392/202866528-7f832202-4821-4cf7-ab19-002c373746bb.png)

Tracing code for another correct sample would be:

![image](https://user-images.githubusercontent.com/77017392/202863273-81a102bb-6986-467a-84e8-527be405efcf.png)

Tracing code for incorrect sample would be:

![image](https://user-images.githubusercontent.com/77017392/202863298-c323bdfb-7174-4665-bb39-b9e4d765cb55.png)

Tracing code for another incorrect sample would be:

![image](https://user-images.githubusercontent.com/77017392/202863330-7a724c55-85ea-4fa6-af9d-aabc8aae65ed.png)




