import vlc
import subprocess
import os
import time

def event_callback(event):
  """Handles VLC media player events."""
  # Check for specific events (e.g., playback end)
  if event.type == vlc.EventType.MediaPlayerEndReached:
    print("Playback finished, moving to next video.")

def play_video_fullscreen(video_path):
  """Plays a video using VLC in full screen and handles events."""
  instance = vlc.Instance()
  player = instance.media_player_new()
  media = instance.media_new(video_path)
  player.set_media(media)

  # Set full screen mode
  player.set_fullscreen(True)

  player.play()

  # Use get_event if available for efficient event handling
  if hasattr(player, 'get_event'):
    event_manager = player.event_manager()
    event_manager.event_attach(vlc.EventType.MediaPlayerEndReached, event_callback)
  else:
    print("get_event not available, using loop for basic event handling.")
    while True:
      time.sleep(0.1)
      if player.get_state() == vlc.State.Ended:
        break

  player.release()
  instance.release()

if __name__ == "__main__":
  # Replace with a list of video paths
  path =  "/home/yogesh/pi_files/media"

  for file in os.listdir(path):
    file = path + "/" + file
    if file.endswith("mp4"):
      play_video_fullscreen(file)