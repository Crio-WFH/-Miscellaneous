#!/usr/bin/python3


import cgi
import subprocess as sp


print('content-type:text/html')
print()

f=cgi.FieldStorage()
cmd=f.getvalue("x")
cmd1=f.getvalue("y")



output=sp.getoutput(f'kubectl run {cmd} --image={cmd1} --kubeconfig admin.conf')
print(output)





print("\n\nPod created successfully!!")






