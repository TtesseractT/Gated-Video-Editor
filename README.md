# Gated Video Editor 

This takes the natural gaps out of videos with dialogue.

**Install**

Run `Setup-Gate-Engine.py`

This will run all requirements for you.

**Prerequisite** 

Python 3.11 or higher

**Standalone**

You can use the script Gated-Engine.py as a seperate argument see TOOLS Below.

**TOOLS**

>python Gate-Engine.py --input_file Video.mp4 --output_file VideoMP4_Output.mp4 --sounded_speed 1 --silent_speed 999999 --frame_margin 3

`--input_file` = Input File you want to process.

`--url` = A youtube url to download and process.

`--output_file` = the output file. (optional. if not included, it'll just modify the input file name).

`--silent_threshold`, `default=0.03` = The volume amount that frames' audio needs to surpass to be consider \"sounded\". It ranges from 0 (silence) to 1 (max volume).

`--sounded_speed`, `default=1.00` = The speed that sounded (spoken) frames should be played at. Typically 1.

`--silent_speed`, `default=5.00` = The speed that silent frames should be played at. 999999 for jumpcutting.

`--frame_margin`, `default=1` = Some silent frames adjacent to sounded frames are included to provide context. How many frames on either the side of speech should be included? That's this variable.

`--sample_rate`, `default=44100` = Sample rate of the input and output videos.

`--frame_rate`, `default=30` = Frame rate of the input and output videos. optional... I try to find it out myself, but it doesn't always work.

`--frame_quality`, `default=3` = Quality of frames to be extracted from input video. 1 is highest, 31 is lowest, 3 is the default.
