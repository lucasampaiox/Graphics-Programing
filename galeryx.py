from tkinter import * 
from PIL import ImageTk, Image

root = Tk()
root.title("Image viewer")
root.geometry("610x430")
root.iconbitmap("images/icon.ico")

image1 = ImageTk.PhotoImage(Image.open(r"images\image.jpg").resize((600, 350)))
image2 = ImageTk.PhotoImage(Image.open(r"images\115614371-e7dcfb7b5ea54e9d229595bf56e51857.jpg").resize((600, 350)))
image3 = ImageTk.PhotoImage(Image.open(r"images\F_iziywWcAE_Zgn.jpg").resize((600, 350)))
image4 = ImageTk.PhotoImage(Image.open(r"images\vih.jpg").resize((600, 350)))
image5 = ImageTk.PhotoImage(Image.open(r"images\mari.png").resize((600, 350)))
images_list = [image1, image2, image3, image4, image5]
counter = 0

def ChangeImage():
  global counter
  if counter < len(images_list) - 1:
    counter += 1
  else:
    counter = 0
  print(counter)
  imgLabel.config(image=images_list[counter])
  infoLabel.config(text="Image " + str(counter + 1) + " of " + str(len(images_list)))

imgLabel = Label(root, image="")
infoLabel = Label(root, text="Image 1 of 5", font="Helvetica, 20")
button = Button(root, text="Change", width=20, height=2, bg="purple", fg="white", command=(ChangeImage))

imgLabel.pack()
infoLabel.pack()
button.pack(side="bottom", pady=3)

root.mainloop()