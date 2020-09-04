import cv2
import datetime
from typing import Tuple
from tabulate import tabulate

def prettify_video_info(video_file: str, frame_count: int, fps: int, length: float, width:int, height:int):
    """ Returns a prettified formatted string with all the frame_generator data.

    :param video_file: video_file.
    :param frame_count: number of frames in the frame_generator.
    :param fps: fps of the frame_generator.
    :param length: length of the frame_generator in seconds.
    :param width: width of the frames in the frame_generator.
    :param height: height of the frames in the frame_generator.
    :return: prettified string containing all the frame_generator data ready for displaying it to the user.
    """
    pretty_length = str(datetime.timedelta(seconds=int(length)))
    headers = ["Attribute", "Value"]
    table = [["File", video_file],
            ["Frame count", frame_count],
            ["FPS", fps],
            ["Length", pretty_length],
            ["Resolution", "{0}x{1}".format(width, height)]]
    return tabulate(table, headers, tablefmt="fancy_grid")


def get_video_info(video_file: str) -> Tuple[str, int, int, float, int, int]:
    """ Extracts frame_generator info (see return) from a frame_generator file with the help of opencv. The
        length of the frame_generator is returned in seconds.

    :param video_file: frame_generator file of which the info is returned
    :return: Tuple(video_file, frame_count, fps, length_in_seconds, frame_height, frame_width)
    """
    cap = cv2.VideoCapture(video_file)
    if not cap.isOpened():
        raise ValueError("could not open frame_generator file: {0}".format(video_file))

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = cap.get(cv2.CAP_PROP_FPS)
    length = frame_count/fps
    return video_file, frame_count, fps, length, height, width
