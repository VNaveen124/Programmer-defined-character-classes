#regexprex3.py
import re
matinfo=re.finditer("[kvr]","Ak#4v@R5$Vw%rP")
print("------------------------------------------------------------------")
for mat  in matinfo:
	print("start Index: {}\t End Index: {}\t Value: {}".format(mat.start(),mat.end(),mat.group()))
else:
	print("------------------------------------------------------------------")
