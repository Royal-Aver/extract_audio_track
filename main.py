import moviepy.editor

video = moviepy.editor.VideoFileClip('video/The_Cranberries_Zombie.mp4')

audio = video.audio
audio.write_audiofile('video/Zombie.mp3')