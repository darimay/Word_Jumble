Word_Jumble
===========
This is the code for the following challenge:

Can you create a program to solve a word jumble? (More info here: http://en.wikipedia.org/wiki/Jumble) The program should accept a string as input, and then return a list of words that can be created using the submitted letters. For example, on the input "dog", the program should return a set of words including "god", "do", and "go".

Please implement the program in a language of your choice, but refrain from using any combinatorics helper modules or imports (e.g. itertools in Python). In order to verify your words, just download an English word list (here are a few: http://wordlist.sourceforge.net/).

Main function: word_jumble
use case: 
```
>> from jumble import word_jumble
>> word_jumble('dog', word_list)
['do', 'go', 'god']
```

word_list should be a list of strings.


running the tests:
```
>> from jumble import test
>> test()
Time it took to generate the full list: 0.612 secs
```
should run without any assertion errors.
