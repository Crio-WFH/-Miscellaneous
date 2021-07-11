#!/bin/python3

import cgi
import subprocess as sp

print("content-type:text/html")
print()


f = cgi.FieldStorage()

d1=f.getvalue("del_podname")

d=sp.getoutput('kubectl delete pod '+d1+' --kubeconfig admin.conf')

print(d)

print(f"\n\nPod {d1} Deleted Successfully ...... \n\n")




