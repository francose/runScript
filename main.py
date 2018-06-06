'''

Author : Sadik Erisen
Purpose : Help to activate the environment

1. cd <path>
2. ifconfig
3. ip variable = ip addr
4. source bin/activate
5. cd <path>
6. python manage.py ip:8000


'''



#! /usr/bin/python
#! /bin/sh
#! /usr/bin/env bash
import os, sys, socket, pdb, time
from  subprocess import PIPE, Popen


#get firsrt pwd
current_path = os.getcwd()
#print(current_path) # test cp

#get recent IP addr
# def system_call(command):
#     p = Popen([command], stdout=PIPE, shell=True)
#     return p.stdout.read()
#
# def get_gateway():
#     return system_call("route -n get default | grep 'gateway' ")
#


target_dir = ''
list_items = os.listdir(target_dir)
print list_items
#
#
#
def is_venv():
    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

if('bin'in list_items):
    os.chdir('')
    newCurrentPath = os.getcwd()
    print ('\n\n','Accesing to .. ', newCurrentPath, '\n\n')
    time.sleep(1)

    ENV_ = os.getcwd()
    newTarget_Dir = os.listdir('')

    # if ('activate' in newTarget_Dir ):
        #! /Volumes/HD2/Projects/EEGScript/bin/python3.5

    Popen('/bin/bash --rcfile  source bin/activate && cd /src && python manage.py runserver ', stdout=PIPE ,shell=True, executable='/bin/bash')
    print('Activating env ... ')

    if is_venv():
        print('inside virtualenv or venv')
    else:
        print('outside virtualenv or venv')

    time.sleep(1)

else:
   print('ERROR')
