"""
jobs.py

Show a simple example of how to define a custom job and pass it to the ZdmClient.

"""
import json
import time

from zdm import ZDMClient

device_id = 'dev-4vhcbbtc80cl'# *** PUT YOU DEVICE ID HERE ***'
password = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkZXYtNHZoY2JidGM4MGNsIiwidXNlciI6ImRldi00dmhjYmJ0YzgwY2wiLCJrZXkiOjEsImV4cCI6MjUxNjIzOTAyMn0.MucxCuzHF9lPLb4j8dYd519vP215k1P4LyuGODYDxvU' # *** PUT YOUR PASSWORD HERE ***'

def set_temp(zdmclient, args):
    # zdmclient: is the object of the ZdmClient.
    # args     : is a json with the arguments  of the function.
    print("Executing job set_temp. Received args: {}".format(args['ciao']))
    # DO SOMETHING
    # return: a json with the result of the job.
    return json.dumps({"msg": "Temperature set correctly."})


# A dictionary of jobs where the key is the name of the job and value if the callback to execute.
my_jobs = {
    "set_temp": set_temp,
}

device = ZDMClient(device_id=device_id, jobs=my_jobs, endpoint="mqtt.zdm.test.zerynth.com")
device.set_password(password)
device.connect()

while True:
    time.sleep(3)
