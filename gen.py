import glob, os, sys

#d = 'en/2007'
d = sys.argv[1] # param is like en/2007
for f in glob.glob(d + '/*/*.md'):
    fin = open(f)
    for line in fin.readlines():
        ff = f.replace(d, '')[1:]
        print ("[%s](%s)\n" % (line[2:].strip(), ff))
        break
    
