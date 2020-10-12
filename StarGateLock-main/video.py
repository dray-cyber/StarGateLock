import time
import tkinter as tk
import imageio
from PIL import Image, ImageTk
pause_video = False
# download video at: http://www.html5videoplayer.net/videos/toystory.mp4
video_name = "wormhole.mp4"
video = imageio.get_reader(video_name)

def video_frame_generator():
    def current_time():
        return time.time()

    start_time = current_time()
    _time = 0
    for frame, image in enumerate(video.iter_data()):

        # turn video array into an image and reduce the size
        image = Image.fromarray(image)
        image.thumbnail((750, 750), Image.ANTIALIAS)

        # make image in a tk Image and put in the label
        image = PhotoImage(file=image)

        # introduce a wait loop so movie is real time -- asuming frame rate is 24 fps
        # if there is no wait check if time needs to be reset in the event the video was paused
        _time += 1 / 24
        run_time = current_time() - start_time
        while run_time < _time:
            run_time = current_time() - start_time
        else:
            if run_time - _time > 0.1:
                start_time = current_time()
                _time = 0

        yield frame, image

def _start():
    global pause_video
    pause_video = False
movie_frame = video_frame_generator()
while True:
    if not pause_video:
        frame_number, frame = next(movie_frame)
        my_label.config(image=frame)

    root.update()

root.mainloop()