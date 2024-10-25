# piads
# Reminder: This can be executed only on raspberry pi.
- In this the main goal is to show or preview advertisements using raspberri pi.
- The first step i have done is to take a raspberry pi (you can use any version) then i just created a python file and i wrote the script to run the code
then to run the advertisements i have created a service file to run in the background while the pi is booting or getting started.
- i just wrote the code in such a way that the adds(videos) can be played on the startup ,now you may think i have created a media file but i have limited videos and i wanted to add new video files into it.
- So i have created a web page where you can upload and download the videos.
- For frontend i used html and css and for backend i used python for uploading and downloading the video.

## Installation and Execution

pi requires [python](https://python.org) v10+ and some of the library files to run.

Install the dependencies and devDependencies and start the server.

```sh
cd <folder name>
python piads.py
```
This is used to run the script manually

For automation

```ssh
sudo systemd enable video_player.service
sudo systemd start video_player.service
sudo systemd status video_player.service
```
- The first one enables the script to run,
- Second one starts the process,
- Third one checks the status if it is working correctly or not,
- And finally you are good to go.
- But if you face any issues while running the service then use this:
  
```ssh
sudo systemctl daemon-reload
sudo systemd restart video_player.service
```
- This reloads the service file and restarts the service file.

- For executon for web app use vs code and add the given files into it.
- run the python file as:

```ssh
python web_app.py
```
- This executes and it opens a web portal where you can download and upload the video files
 
