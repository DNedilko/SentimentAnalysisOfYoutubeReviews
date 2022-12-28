import youtube_dl
import os
import ffmpeg



playlist = ['https://youtu.be/DbmzO0K4NtQ','https://youtu.be/VwcOYOujmiY','https://youtu.be/XrY9hXaMpug','https://youtu.be/_PLQV6zmcjE']
url_playlist = 'https://www.youtube.com/playlist?list=PLa-rIqkPf3pFZitDmzHA_VCZTwuc0yEIQ'
destination = './PreStuding/reviews'

ydl_opts = {'outtmpl': f'{destination}/%(title)s.%(ext)s'}
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
     # ydl.download([playlist[1]])

filenames = next(os.walk(destination), (None, None, []))[2]
print(f"Old file names {filenames}")
for num, name in enumerate(filenames):
    n = name.split(".")[0]
    ext = name.split(".")[-1]
    os.rename(destination+"/" +name , destination+"/"+ str(num+2) + "." + ext)

command = f'ffmpeg -i {destination}/2.mkv -acodec pcm_s16le -ar 16000 -ac 1 ./PreStuding/wav_data_reviews/2.wav'
os.system(command)

new_filenames = next(os.walk(destination), (None, None, []))[2]
for name in new_filenames:
    n = name.split(".")[0]
    command = f'ffmpeg -i {destination}/{name} -acodec pcm_s16le -ar 16000 -ac 1 ./PreStuding/wav_data_reviews/{n}.wav'
    os.system(command)


wav_filenames_ = next(os.walk("."), (None, None, []))[2]
wav_filenames = next(os.walk("./PreStuding/wav_data_reviews"), (None, None, []))[2]
print(f'New filenames {wav_filenames}')