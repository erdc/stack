import os
ignored={}
PATH=''
LD_LIBRARY_PATH=''
PROLOGUE=''
for k,v in os.environ.items():
    if os.environ['USER'] in v:
        ignored[k] = v
    else:
        PROLOGUE+='export {0}="{1}"; '.format(k,v)

for p in ignored['LD_LIBRARY_PATH'].split(":"):
    if os.environ['USER'] not in p:
        LD_LIBRARY_PATH+=":{0}".format(p)
PROLOGUE="export LD_LIBRARY_PATH={0}; ".format(LD_LIBRARY_PATH)+PROLOGUE
del ignored['LD_LIBRARY_PATH']
for p in ignored['PATH'].split(":"):
    if os.environ['USER'] not in p:
        PATH+=":{0}".format(p)
PROLOGUE="export PATH={0}; ".format(PATH)+PROLOGUE
del ignored['PATH']
#print "Ignoring these paths"
#for k,v in ignored.items():
#    print k+"="+v

print("  PATH: |\n    {0}".format(PATH))
print("  PROLOGUE: |\n    {0}".format(PROLOGUE))


