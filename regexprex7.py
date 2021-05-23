#regexprex7.py
#search for all Capital alphabets only
import re
matinfo=re.finditer("[A-Z]","Ak#4v@aR5g$Vw%rP")
print("------------------------------------------------------------------")
for mat  in matinfo:
	print("start Index: {}\t Value: {}".format(mat.start(),mat.group()))
else:
	print("------------------------------------------------------------")
