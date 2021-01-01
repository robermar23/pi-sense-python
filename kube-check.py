import os
from kubernetes import client, config
from sense_hat import SenseHat

sense = SenseHat()

config.load_kube_config()
v1 = client.CoreV1Api()


row = 0
col = 0
red = (255, 0, 0)
green = (0, 255, 0)

#iterate over nodes and get status of each
response = v1.list_node()
for node in response.items:
    #iterate
    for cond in node.status.conditions:
        if cond.type == "Ready":
            if cond.status == "True":
                sense.set_pixel(row, col, green)
            else:
                sense.set_pixel(row, col, red)
        else:
            if cond.status == "True":
                sense.set_pixel(row, col, red)
            else:
                sense.set_pixel(row, col, green)
