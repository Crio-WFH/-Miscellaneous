#!/usr/bin/python3

import cgi
import subprocess as sp

print("content-type:text/html")
print()

f = cgi.FieldStorage()

#d=f.getvalue("deploy_name")
#r=f.getvalue("replicas")

d="d1"
r="4"
s=sp.getoutput(f"kubectl scale deployment {d} --replicas={r} --kubeconfig admin.conf")
print(s)
print(f"\n\n {r} replicas created successfully ....\n")
