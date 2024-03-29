# Gated Video Editor

Gated Video Editor is a Python script that modifies video files, speeding up silent parts without affecting the sound parts. This is especially useful for instructional videos, as it helps users to watch videos more efficiently without missing any relevant content.

## Table of Contents

- [Gated Video Editor](#gated-video-editor)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Quick install](#quick-install)
  - [Standalone](#standalone)
  - [TOOLS](#tools)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Docker Setup](#docker-setup)
  - [License](#license)

## Prerequisites

- Python 3.6+
- FFmpeg

## Quick install

```bash
./Setup-Gate-Engine.py
```

This will run all requirements for you.

## Standalone

You can use the script `Gated-Engine.py` as a seperate argument

## TOOLS

>python Gate-Engine.py --input_file Video.mp4 --output_file VideoMP4_Output.mp4 --sounded_speed 1 --silent_speed 999999 --frame_margin 3

| Argument | Description |
| --- | --- |
| `--input_file` | Input File you want to process. |
| `--url` | A youtube url to download and process. |
| `--output_file` | the output file. (optional. if not included, it'll just modify the input file name). |
| `--silent_threshold`, `default=0.03` | The volume amount that frames' audio needs to surpass to be consider \"sounded\". It ranges from 0 (silence) to 1 (max volume). |
| `--sounded_speed`, `default=1.00` | The speed that sounded (spoken) frames should be played at. Typically 1. |
| `--silent_speed`, `default=5.00` | The speed that silent frames should be played at. 999999 for jumpcutting. |
| `--frame_margin`, `default=1` | Some silent frames adjacent to sounded frames are included to provide context. How many frames on either the side of speech should be included? That's this variable. |
| `--sample_rate`, `default=44100` | Sample rate of the input and output videos. |
| `--frame_rate`, `default=30` | Frame rate of the input and output videos. optional... I try to find it out myself, but it doesn't always work. |
| `--frame_quality`, `default=3` | Quality of frames to be extracted from input video. 1 is highest, 31 is lowest, 3 is the default. |

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your_username/Gated-Video-Editor.git
```

2. Navigate to the project directory:

```bash
cd Gated-Video-Editor
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the `run.py` script and follow the prompts:

```bash
python run.py
```

2. Alternatively, you can use the Gate-Engine.py script with command line arguments. See below for a list of arguments:

```bash	
python Gate-Engine.py --input_file INPUT_FILE --output_file OUTPUT_FILE --sounded_speed 1 --silent_speed 999999 --frame_margin 3 --frame_rate FRAME_RATE
```

## Docker Setup

1. Build the Docker image:

```bash
docker build -t gated-video-editor .
```

2. Run the Docker container:

```bash
docker run -it --rm -v /path/to/your/video/files:/app gated-video-editor
```

3. Replace `/path/to/your/video/file`s with the path to the directory containing your video files. This will mount the directory inside the container.

## License

This project is released under the MIT License.
