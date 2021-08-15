"""
A very simple GUI image viewer using Tkinker.

Image sources:
https://www.pexels.com/photo/woman-in-black-blazer-and-black-hat-7433162/
https://www.pexels.com/photo/woman-in-white-tank-top-holding-pizza-8148690/
https://www.pexels.com/photo/nature-bush-animals-giraffe-6790685/
https://www.pexels.com/photo/young-woman-standing-in-shadow-near-wall-7159608/
https://www.pexels.com/photo/thoughtful-young-woman-sitting-near-window-4335608/
https://www.pexels.com/photo/light-sea-city-dawn-7332786/
"""

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')

my_img1 = Image.open('images/pexels-damian-barczak-8148690.jpg')
my_img1 = my_img1.resize((400, 600), Image.ANTIALIAS)
my_img1 = ImageTk.PhotoImage(my_img1)

my_img2 = Image.open("images/pexels-elijah-o'donnell-4335608.jpg")
my_img2 = my_img2.resize((400, 600), Image.ANTIALIAS)
my_img2 = ImageTk.PhotoImage(my_img2)

my_img3 = Image.open('images/pexels-lelani-badenhorst-6790685.jpg')
my_img3 = my_img3.resize((400, 600), Image.ANTIALIAS)
my_img3 = ImageTk.PhotoImage(my_img3)

my_img4 = Image.open('images/pexels-olya-prutskova-7433162.jpg')
my_img4 = my_img4.resize((400, 600), Image.ANTIALIAS)
my_img4 = ImageTk.PhotoImage(my_img4)

my_img5 = Image.open('images/pexels-maria-camila-castaÃ±o-7332786.jpg')
my_img5 = my_img5.resize((400, 600), Image.ANTIALIAS)
my_img5 = ImageTk.PhotoImage(my_img5)

my_img6 = Image.open('images/pexels-gantas-vaiÄiulÄnas-7159608.jpg')
my_img6 = my_img6.resize((400, 600), Image.ANTIALIAS)
my_img6 = ImageTk.PhotoImage(my_img6)

"""
Putting all images into a list so displaying images code will be easier to
put together.
"""
image_list = [
    my_img1,
    my_img2,
    my_img3,
    my_img4,
    my_img5,
    my_img6
]

file_names = [
    'pexels-damian-barczak-8148690.jpg',
    "pexels-elijah-o'donnell-4335608.jpg",
    'pexels-lelani-badenhorst-6790685.jpg',
    'pexels-olya-prutskova-7433162.jpg',
    'pexels-maria-camila-castaÃ±o-7332786.jpg',
    'pexels-gantas-vaiÄiulÄnas-7159608.jpg'
]

image_label = Label(image=my_img1)
file_name_label = Label(root, text=file_names[0])
image_number = Label(root, text='Image 1 of {0}'.format(len(image_list)))

index = 0


def change_image(change):
    """
    Displays images back and forth.
    :param change: char value ('b' -> backwards or 'f' -> forward)
    """
    global image_label
    global index
    global file_name_label
    global image_number

    """
    If we're going backwards and we don't go below the lowest index in the
    next step, the program will display the previous image.
    """
    if change == 'b' and index - 1 >= 0:
        image_label.grid_forget()
        index -= 1
        """
        Re-create the label displaying images and display the previous 
        image in the list.
        """
        image_label = Label(image=image_list[index])
        image_label.grid(row=0, column=0, columnspan=3)
        file_name_label.destroy()
        file_name_label = Label(root, text=file_names[index])
        file_name_label.grid(row=1, column=0, columnspan=3)
        image_number.destroy()
        image_number = Label(root,
                             text='Image {0} of {1}'.format(index+1,
                                                            len(image_list)))
        image_number.grid(row=3, column=0, columnspan=3, sticky=W + E)

    """
    If we're going forwards and we don't go above the highest index in the 
    next step, the program will display the next image.
    """
    if change == 'f' and index + 1 < len(image_list):
        image_label.grid_forget()
        index += 1
        """
        Re-create the label displaying images and display the next
        image in the list.
        """
        image_label = Label(image=image_list[index])
        image_label.grid(row=0, column=0, columnspan=3)
        file_name_label.destroy()
        file_name_label = Label(root, text=file_names[index])
        file_name_label.grid(row=1, column=0, columnspan=3)
        image_number.destroy()
        image_number = Label(root,
                             text='Image {0} of {1}'.format(index+1,
                                                            len(image_list)))
        image_number.grid(row=3, column=0, columnspan=3, sticky=W + E)


button_backward = Button(root, text='<<', padx=20, pady=20,
                         command=lambda: change_image('b'))
button_exit = Button(root, text='EXIT', padx=20, pady=20, command=root.quit)
button_forward = Button(root, text='>>', padx=20, pady=20,
                        command=lambda: change_image('f'))

image_label.grid(row=0, column=0, columnspan=3)
file_name_label.grid(row=1, column=0, columnspan=3)
button_backward.grid(row=2, column=0)
button_exit.grid(row=2, column=1)
button_forward.grid(row=2, column=2)
image_number.grid(row=3, column=0, columnspan=3, sticky=W + E)

root.mainloop()
