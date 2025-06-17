# PIADS

- The main goal of this project is to show (or) display advertisement videos using raspberry pi for promoting products for a specific company (or) companies which    provides it's videos to bring awareness in the market and attract people.
- // you may use any board you want
- The first step i have done is :
  - I have taken raspberry pi (any version).
- Second step : 
  - I have created two python files where one is the main file for displaying ads and the other one is for uploading videos.
- Third step :
  - I wrote the script to exectue the code.
- To run the advertisements (or) videos , i have created a service file (video_player.service) to be executed in the background while the pi is booting (or)          getting started.
- I wrote the logic in such a way that ads (or) videos can be played on the startup of a cpu (or) booting of pi.
- Now you may think that i have created a media folder , but it contains only few videos!! , and you wanted to add new video files into it.
- So i have created a web page where you can upload the videos and it stores the videos directly into the media folder and also you can see the uploaded videos.
- For Frontend i have used html and css and for Backend i have used python-flask for uploading the video and displaying the uploaded videos to verify that the        uploaded video is correct or not.

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
- This executes and it opens a web portal where you can upload the video files and view the videos.
 
