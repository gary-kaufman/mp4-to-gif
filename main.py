from moviepy.editor import *


def mkv_to_gif():
    video_clip = VideoFileClip("video-for-gif.mp4")

    video_clip.write_gif("output.gif", fps=15, logger='bar')


if __name__ == '__main__':
    mkv_to_gif()
