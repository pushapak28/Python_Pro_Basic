# pip install pytube

import pytube

link= input('Enter You tube Video URL\n')
yt = pytube.YouTube(link)
yt.streams.first().download()
print("Downloaded", link)
