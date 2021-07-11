#!/usr/bin/python3

import cgi
import subprocess as sp

print("content-type:text/html")
print()

d=sp.getoutput("kubectl delete all --all --kubeconfig admin.conf")
print(d)

print("All resources are deleted successfully.....\n\n")
