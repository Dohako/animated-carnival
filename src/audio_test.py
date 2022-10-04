import cv2
import numpy as np
#ffpyplayer for playing audio
from ffpyplayer.player import MediaPlayer
import ffmpeg
import wave
from moviepy.editor import VideoFileClip

video_path="./derevyashki_1.mp4"
def PlayVideo(video_path):
    video=cv2.VideoCapture(video_path)
    video_out = cv2.VideoWriter('video.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (854,480))
    # audio_out = cv2.VideoWriter('audio.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (854,480))
    player = MediaPlayer(video_path)
    audio_frames = []
    while True:
        grabbed, frame=video.read()

        audio_frame, val = player.get_frame()

        # audio_out.write(audio_frame)
        video_out.write(frame)
        print(audio_frame)
        print(val)
        audio_frames.append(audio_frame)

        

        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
            cv2.imshow("Audio", img)

    # rate=44100
    # channels=2
    # waveFile = wave.open("./audio_out.wav", 'wb')
    # waveFile.setnchannels(channels)
    # waveFile.setsampwidth(2)
    # waveFile.setframerate(rate)
    # waveFile.writeframes(b''.join(audio_frames))
    # waveFile.close()
    # video = VideoFileClip(video_path) # 2.
    # audio = video.audio # 3.
    # audio.write_audiofile("audio.wav") # 4.
    video_out.release()
    video.release()
    cv2.destroyAllWindows()
PlayVideo(video_path)