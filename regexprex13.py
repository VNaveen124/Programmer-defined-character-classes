#regexprex13.py
#search for all  except Alphabets--small and capital
import re
matinfo=re.finditer("[A-Za-z0-9]","Ak#4v@aR5g$Vw%8rP")
print("------------------------------------------------------------------")
for mat  in matinfo:
	print("start Index: {}\t Value: {}".format(mat.start(),mat.group()))
else:
	print("----------------------------------------------------------")
