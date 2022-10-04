import os
from typing import Union
import cv2


class VideoCleaner:
    def __init__(self) -> None:
        ...

    def clean_video(self, path_to_file: Union[list[str], str], combine_videos: bool = False):
        
        if isinstance(path_to_file, list):
            for path in path_to_file:
                ...
        elif isinstance(path_to_file, str):
            if os.path.isfile(path_to_file) is False:
                raise FileNotFoundError
            self._clean(path_to_file)
        else:
            raise TypeError

    def _clean(self, path_to_file: str):
        video = cv2.VideoCapture(path_to_file)
        out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (854,480))

        # Check if camera opened successfully
        if (video.isOpened()== False): 
            print("Error opening video stream or file")

        # Read until video is completed
        while(video.isOpened()):
        # videoture frame-by-frame
            ret, frame = video.read()
            # print(frame.shape)
            if ret == True:
                out.write(frame)
                # Display the resulting frame
                cv2.imshow('Frame',frame)

                # Press Q on keyboard to  exit
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

            # Break the loop
            else: 
                break

        # When everything done, release the video videoture object
        video.release()
        out.release()

        # Closes all the frames
        cv2.destroyAllWindows()