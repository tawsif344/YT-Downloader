clear;echo;echo 'Install the package...';sleep 2;pkg update;pkg upgrade;clear;termux-setup-storage;pkg install python;pip install youtube-dl;pkg install ffmpeg;mkdir /data/data/com.termux/files/home/storage/shared/Downloader;mkdir -p ~/.config/youtube-dl;echo '--no-mtime
-o /data/data/com.termux/files/home/storage/shared/Downloader/%(title)s.%(ext)s
-f "best[height<=360]"' > ~/.config/youtube-dl/config;mkdir ~/bin;echo 'youtube-dl $1' > ~/bin/termux-url-opener;echo;echo 'Install Successfully'
