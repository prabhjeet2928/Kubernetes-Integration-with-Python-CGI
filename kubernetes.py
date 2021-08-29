#!/usr/bin/python3

import time
import cgi
import subprocess

print("content-type: text/html")
print()

field = cgi.FieldStorage()
key = field.getvalue("key")
cmd1 = field.getvalue("x")
cmd2 = field.getvalue("y")

if key=="Pod/Deployment":
	run = "kubectl get pods"

elif key=="Services":
	run = "kubectl get svc"

elif key=="launchpod":
	run = "kubectl run {} --image={}".format(cmd1,cmd2)

elif key=="podDeployment":
	run = "kubectl create deployment {} --image={}".format(cmd1,cmd2)

elif key=="scaleReplica":
	run = "kubectl scale deployment {} --replicas={}".format(cmd1,cmd2)

elif key=="portNumber":
	temp = subprocess.getoutput("sudo kubectl expose deployment {} --port={} --type=NodePort".format(cmd1, cmd2))

	time.sleep(1)
	run = "kubectl get svc"

elif key=="freeResource":
	run = "kubectl delete service {}".format(cmd1)

elif key=="delEnv":
	if cmd1=="Pod":
		run = "kubectl delete pod {}".format(cmd2)
	else:
		run = "kubectl delete deployments {}".format(cmd2)

else:
	run = "echo 'Something went wrong. Please try again later'"
	
output = subprocess.getoutput("sudo " + run)
print(output)