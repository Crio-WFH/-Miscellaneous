#!/usr/bin/python3

import cgi
import subprocess as sp

print("content-type:text/html")
print()

f = cgi.FieldStorage()


del_deploy_name = f.getvalue("del_deployname")

del_deploy =  sp.getoutput('kubectl delete deployment  '+del_deploy_name+' --kubeconfig admin.conf')

print(del_deploy)

print("\n\nDeployment {} Deleted Successfully ...... \n\n".format(del_deploy_name))
