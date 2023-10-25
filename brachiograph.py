import pyrebase as pb
from brachiograph import BrachioGraph
from linedraw import *
import json

# our database
config = json.load(open("config.json"))

# download image from database
firebase = pb.initialize_app(config)
storage = firebase.storage()
path_on_cloud = 'images/pic.jpg'
storage.child(path_on_cloud).download(path_on_cloud,'images/image.jpg')
image_to_json('image', draw_contours=2, draw_hatch=16) # can edit these arguments based on image

# create BrachioGraph instance
bg= BrachioGraph(inner_arm=10.87,
                 outer_arm=11.13,
                 bounds=[15, 7, 6, 15],
                 servo_1_centre=1710,
                 servo_2_centre= 1370,
                 hystereis_correction_1=10,
                 hystereis_correction_2=2)

bg.plot_file('images/image.json') # draw 