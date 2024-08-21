from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips
from moviepy.editor import vfx
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import play

# Memuat file video
video = VideoFileClip('videoAnimasi.mp4')

# Menyimpan file video
video.write_videofile('result_video.mp4')


#crop
short_video = video.subclip(0, 10)  # Mendapatkan 10 detik pertama
short_video.write_videofile('short_result.mp4')

#gabungkan 2 vid

combined_video = concatenate_videoclips([video, short_video])
combined_video.write_videofile('combined_result.mp4')

#reverse
reversed_video = short_video.fx(vfx.time_mirror)  # Membalikkan video
reversed_video.write_videofile('reversed_result.mp4')


#mempercepat
sped_up_video = short_video.fx(vfx.speedx, 2)  # Mempercepat video 2x
sped_up_video.write_videofile('sped_up_result.mp4')


# Membuat jendela utama
root = tk.Tk()
root.title("LAB MULTIMEDIA")

# Menjalankan loop acara Tkinter


# Memuat gambar menggunakan Pillow
image = Image.open('kucing.jpg')
photo = ImageTk.PhotoImage(image)

# Membuat label untuk menampilkan gambar
label = tk.Label(root, image=photo)
label.pack()

# Definisikan fungsi untuk memutar musik
def play_music():
    file_path = filedialog.askopenfilename()
    if file_path:
        audio = AudioSegment.from_file(file_path)
        play(audio)

# Membuat tombol untuk memutar musik
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

root.mainloop()