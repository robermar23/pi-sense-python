import os
from kubernetes import client, config
from sense_hat import SenseHat

print ("Starting kube-check")

try:
    sense = SenseHat()
    sense.clear()
except Exception as e:
    print(e)

try:
    config.load_kube_config(config_file="/home/pi/.kube/admin.conf")
except Exception as e:
    print(e)

try:
    v1 = client.CoreV1Api()

    row = 0
    col = 0
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    #iterate over nodes and get status of each
    response = v1.list_node()
    for node in response.items:
        #iterate
        col = 0
        for cond in node.status.conditions:
            if cond.type == "Ready":
                if cond.status == "True":
                    sense.set_pixel(col, row, green)
                else:
                    sense.set_pixel(col, row, red)
            else:
                if cond.status == "True":
                    sense.set_pixel(col, row, red)
                else:
                    sense.set_pixel(col,row, green)
            col = col + 1
        row = row + 1
except Exception as e:
    sense.set_pixel(col,row, blue)
    print(e)
finally:
    print ("Ending kube-check")

