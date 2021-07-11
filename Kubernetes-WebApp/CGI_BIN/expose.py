#!/usr/bin/python3

import cgi
import subprocess

print("content-type:text/html")
print()

f = cgi.FieldStorage()


e1=f.getvalue("del_deployname")

e =  subprocess.getoutput(f'kubectl expose deployment  {e1} --type=NodePort --port=80  --kubeconfig admin.conf')
print(e)
print(f"\n\nDeployment {e1} is Exposed ...... \n\n")
