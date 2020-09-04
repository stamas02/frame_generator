import argparse
from frame_generator import FrameGenerator
import cv2


def parseargs():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                     description='''Example to read and display frames from a video''')
    parser.add_argument('--video-file', '-v', type=str, help="path to the video file")

    args = parser.parse_args()
    return args


def play(video_file):
    fg = FrameGenerator(video_source=video_file, show_video_info=True, color_mode="BGR", every_nth_frame=10)
    for frame in fg:
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    args = parseargs()
    play(**args.__dict__)
