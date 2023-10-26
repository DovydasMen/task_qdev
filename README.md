# task_qdev
# Getting started

To use this code you should have atleast python 3.9.6 version. This task mainly designed on local machine.

# Installation

1. Pull source code from Git repository.
2. Install all requirements because of external libraries. Command: pip install -r requirements.txt . Note! You could skip this part, only black formated was used here!
3. In order to use black formater. Activate your virtual environment. Command example: black task_one.py
4. To start test you should type command: python3 -m unittest -v 
5. To start main program type in command: python3 task_one.py

# Tasks

# Exercise 1 
Given a paragraph of text: (the paragraph is provided below) 
	•	Find the number of times each word in the paragraph is used. Print the top 3 most used words. 
	•	Find the shortest sentence from the paragraph. Print the sentence and the number of words in that sentence. 
	•	Print a version of the paragraph in which the first and every other letter from every word is capitalized. (Example: The quick brown fox -> ThE QuIcK BrOwN FoX) 
	•	Print a version of the paragraph in which all words are in reversed order. (Example: The quick brown fox -> fox brown quick The) 
 
text = """The European languages are members of the same family. Their separate existence is a myth. For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words. Everyone realizes why a new common language would be desirable: one could refuse to pay expensive translators. To achieve this, it would be necessary to have uniform grammar, pronunciation and more common words. If several languages coalesce, the grammar of the resulting language is more simple and regular than that of the individual languages. The new common language will be more simple and regular than the existing European languages. It will be as simple as Occidental; in fact, it will be Occidental. To an English person, it will seem like simplified English, as a skeptical Cambridge friend of mine told me what Occidental is.""" 
 
Note! At the moment only this part is finished!
 
# Exercise 2 
You were given a map (2 dimensional grid) where each cell is either forest (marked as X) or grassland (marked as O).  
Write a script that gets number of isolated forests on the map. Forest is formed of cells X that are connected in one of 8 directions. In case code is not working, please explain the search strategy. 
(Example on next page) 
 
 
 
Example: 
There are two forests in the map (red and green) bellow: 
0X0X0 
00XX0 
00000 
0XX00 
 

