#coding:utf-8
#!/usr/bin/python

import sys, os, random, py_compile, string

if len(sys.argv) != 2:
	print('usage : python protect.py <filename>')
elif not os.path.exists(sys.argv[1]):
	print('Error, file not found')

else:
	filename = sys.argv[1]
	fich = open(filename,'r')
	content = fich.read()
	if len(content)<1246:
		reste = 1246-len(content)
		for i in range(reste):
			if i==0:
				content+='#'
			else:
				content+=random.choice(string.ascii_lowercase+string.uppercase)
	out,special='exec str(',False
	print(content)
	x=0
	for caract in content:
		if x<3:
			pass
		elif caract=='\\':
			out+='\'\\'
			special=True
		elif special:
			out+=caract+'\'+'
			special=False
		else:
			out+='unichr({})+'.format(str(ord(caract)))
		x+=1
	out = out[:-1]+')'
	output=open('protected.py','w')
	output.write(out)
	output.close()
	py_compile.compile('protected.py')
	print('Success ! Your python protected file is "protected.pyc"')
