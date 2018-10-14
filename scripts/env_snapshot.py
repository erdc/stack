import os
ignored={}
PATH=''
LD_LIBRARY_PATH=''
PROLOGUE=''
for k,v in os.environ.items():
    if os.environ['USER'] in v:
        ignored[k] = v
    elif k in ['PATH','LD_LIBRARY_PATH','SHELL']:
        ignored[k] = v
    elif 'PYTHON' in k or 'python' in v:
        ignored[k] = v
    elif 'PETSC' in k:
        ignored[k] = v
    elif k == 'SHELL':
        ignored[k] = v
    else:
        PROLOGUE+='export {0}="{1}"; '.format(k,v)

for p in ignored['LD_LIBRARY_PATH'].split(":"):
    if os.environ['USER'] not in p and 'python' not  in p:
        if len(LD_LIBRARY_PATH) != 0:
            LD_LIBRARY_PATH+=":"
        LD_LIBRARY_PATH+="{0}".format(p)
PROLOGUE="export LD_LIBRARY_PATH={0}; ".format(LD_LIBRARY_PATH)+PROLOGUE
del ignored['LD_LIBRARY_PATH']
for p in ignored['PATH'].split(":"):
    if os.environ['USER'] not in p and 'python' not in p:
        if len(PATH) != 0:
            PATH+=":"
        PATH+="{0}".format(p)
PROLOGUE="export PATH={0}; ".format(PATH)+PROLOGUE
del ignored['PATH']
#print "Ignoring these paths"
#for k,v in ignored.items():
#    print k+"="+v
try:
    PROLOGUE+= "export WORKDIR={0}; ".format(
        ignored['WORKDIR'].replace(
            os.environ['USER'],r'${USER}'))
except:
    pass

#compilers
PROLOGUE+="export CC=gcc; export CXX=g++; export F77=gfortran; export F90=gfortran; export FC=gfortran; TERM=xterm; "
print("  PATH: |\n    {0}".format(PATH))
print("  PROLOGUE: |\n    {0}".format(PROLOGUE))


