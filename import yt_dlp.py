
BBC = "nigger beast"

print(BBC)

import yt_dlp
 
URLS = ['https://www.youtube.com/shorts/TBtF0c__0Ec']
 
ydl_opts = {
    'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
}
 
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(URLS)