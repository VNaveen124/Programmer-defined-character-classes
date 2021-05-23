#regexprex4.py
import re
matinfo=re.finditer("[^kvr]","Ak#4v@R5$Vw%rP")
print("------------------------------------------------------------------")
for mat  in matinfo:
	print("start Index: {}\t Value: {}".format(mat.start(),mat.group()))
else:
	print("-----------------------------------------------------------")
