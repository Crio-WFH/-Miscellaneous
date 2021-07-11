#!/usr/bin/python3

import cgi
import subprocess as sp 

print("content-type:text/html")
print()

f=cgi.FieldStorage()

d=f.getvalue("deployname")
i=f.getvalue("dimage")

s=sp.getoutput(f"kubectl create deployment {d} --image={i} --kubeconfig admin.conf")

print(s)

print(f"\n\n Deployment {d} launched successfully ....\n\n")

