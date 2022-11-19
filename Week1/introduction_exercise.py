# For this exercise, you will need to change the value in this section of
# program.
# 
# This assignment will require that you enter your name in the string below.
# So if your name is "Isabel", then the line of code should look like:
#     your_name = "Isabel"
# 
# After you've made this change, save the file.
# Once saved, you must then run the program using the Python interepreter.
# 
# For this program and the rest of this class, you can safely ignore
# everything after the commented line with ten dashes.

your_name = "Isabel"

# ----------

import string
import sys
try:
    from sklearn import preprocessing
except ModuleNotFoundError:
    print("You do not have sklearn installed with this Python interepreter.")
    sys.exit()

le = preprocessing.LabelEncoder()
le.fit(list(''.join([i for i in your_name.lower() if i.isalpha()])))
print( "\n", your_name, sum([ord(c) for c in le.classes_]) )