# Description
frame_generator is a simple python package based on opencv to easily grab
frames from a video files.
#Features
- Creates a generator which iteratively yields the frames from a video file.
- Can skip pre-defined number of frames
- Can choose color mode of the yielded frame
- Allow you to display useful information about a video file.
#Install
```
pip install frame_generator
```

#Usage
###### Reading frames from a video file
Note: the following script will show every 10th frame from the video.
```python
from frame_generator import FrameGenerator

video_file = "PATH/TO/A/VIDEO/FILE"

fg = FrameGenerator(video_source=video_file, 
                    show_video_info=True, 
                    color_mode="BGR", 
                    every_nth_frame=10)
for frame in fg:
    do_something_with_frame(frame)
```
Parameters:

    video_source: str
        path to the frame_generator file you want to read.
    
    show_video_info: bool
        if true then frame_generator info is printed to the console
    
    every_nth_frame: int
        every nth frame will be yielded by the generator. 
        1 means that every single frame will be yielded.
    
    color_mode: str, Optional
        can be 'RGB', 'BGR' or 'Grayscale'
        
###### Getting and displaying video info
```python
from frame_generator.video_info import get_video_info, prettify_video_info

video_file = "PATH/TO/A/VIDEO/FILE"
video_file, frame_count, fps, length, height, width = get_video_info(
    video_file
)
print(prettify_video_info(video_file, 
                          frame_count, 
                          fps, 
                          length, 
                          height, 
                          width))
```
