#######################################################
# Gated Video Editor                                  #
#######################################################
# Built by Sabian Hibbs                               #
# MIT LICENCE                                         #
#######################################################

import os
import subprocess
import re

input_file = input("Please drag and drop the video file here -->: ").strip()
result = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=r_frame_rate', '-of', 'default=noprint_wrappers=1:nokey=1', input_file], stdout=subprocess.PIPE)
frame_rate_str = re.sub('[^0-9/]', '', result.stdout.decode())

num, den = frame_rate_str.split('/')

frame_rate = float(num) / float(den)
output_file = os.path.splitext(input_file)[0] + "_Output" + os.path.splitext(input_file)[1]
cmd = f'python Gate-Engine.py --input_file "{input_file}" --output_file "{output_file}" --sounded_speed 1 --silent_speed 999999 --frame_margin 3 --frame_rate {frame_rate}'
os.system(cmd)
