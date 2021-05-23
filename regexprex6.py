#regexprex6.py
#search for all except small alphabets only
import re
matinfo=re.finditer("[^a-z]","Ak#4v@aR5g$Vw%rP")
print("------------------------------------------------------------------")
for mat  in matinfo:
	print("start Index: {}\t Value: {}".format(mat.start(),mat.group()))
else:
	print("----------------------------------------------------------")
