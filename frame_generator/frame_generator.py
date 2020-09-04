import cv2

from .video_info import get_video_info, prettify_video_info


class FrameGenerator:
    def __init__(
        self, video_source, show_video_info=True, every_nth_frame=1, color_mode="RGB"
    ):
        """
        Init
        Parameters
        ----------
        video_source: str
            path to the frame_generator file you want to read.

        show_video_info: bool
            if true then frame_generator info is printed to the console

        every_nth_frame: int
            every nth frame will be yielded by the generator. 
            1 means that every single frame will be yielded.

        color_mode: str, Optional
            can be 'RGB', 'BGR' or 'Grayscale'
        """

        video_file, frame_count, fps, length, height, width = get_video_info(
            video_source
        )
        if show_video_info:
            print(
                prettify_video_info(
                    video_source, frame_count, fps, length, height, width
                )
            )
        self._frame_count = frame_count
        self.fps = fps
        self.length = length
        self.resolution = (height, width)
        self._cap = cv2.VideoCapture(video_file)
        self._every_nth_frame = every_nth_frame
        self.color_mode = color_mode
        if not self._cap.isOpened():
            raise ValueError("could not open frame_generator file: {0}".format(video_file))

    def __iter__(self):
        """ Read frame from an opencv capture objects and yields
        until this object is not closed.

        Returns
        -------
        a numpy array representing an RGB frame
        """
        cnt = -1
        while self._cap.isOpened():
            ret, frame = self._cap.read()
            cnt += 1
            if cnt % self._every_nth_frame != 0:
                continue
            if frame is None:
                return

            if self.color_mode == "RGB":
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            elif self.color_mode == "Grayscale":
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            yield frame
        self._cap.release()
        raise StopIteration()

    def __len__(self):
        return self._frame_count // self._every_nth_frame
