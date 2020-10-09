## Diaglod Analysis
We’ll be using the dataset available here: https://www.kaggle.com/liury123/my-little-pony-transcript
For the purpose of this study, we’ll use only clean_dialog.csv and assume that the dataset is perfect.
Write a python script named analysis.py that, when run, computes and produces a JSON-formatted analysis of the ponies’ interpersonal dynamics that has exactly the structure given below (all numbers below are just examples). The canonical pony names used in the file should be: twilight (Twilight Sparkle), applejack (Applejack), rarity (Rarity), pinkie (Pinkie Pie), rainbow (Rainbow Dash), and fluttershy (Fluttershy). All other characters are considered “non-Pony” characters.

### scripts/analysis.py
Accept the path to the clean_dialog.csv.
words_alpha.txt is sitting in the data/ directory.
It will be run in a UNIX shell in which PYTHONPATH includes a path to the project’s src directory. This will allow it to use code in the hw3 package.
It should accept an optional argument “-o <file_name>”. If given, the JSON output is written to that file. If it is NOT given, the JSON output should be written to stdout.

## Unit testing

### src/hw3
Include all the analysis function.
test.py(this runs all 10 unit tests.)
tests/ (this directory contains unit tests)
