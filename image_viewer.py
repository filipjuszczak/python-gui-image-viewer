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

# Required imports.
from tkinter import *
from PIL import ImageTk, Image

# Creating the main window.
root = Tk()
# Setting the window title.
root.title('Image Viewer')

# Creating image.
my_img1 = Image.open('images/1.jpg')
# Resizing the image.
my_img1 = my_img1.resize((400, 600), Image.ANTIALIAS)
# Creating a photoimage to use in the program.
my_img1 = ImageTk.PhotoImage(my_img1)

my_img2 = Image.open('images/2.jpg')
my_img2 = my_img2.resize((400, 600), Image.ANTIALIAS)
my_img2 = ImageTk.PhotoImage(my_img2)

my_img3 = Image.open('images/3.jpg')
my_img3 = my_img3.resize((400, 600), Image.ANTIALIAS)
my_img3 = ImageTk.PhotoImage(my_img3)

my_img4 = Image.open('images/4.jpg')
my_img4 = my_img4.resize((400, 600), Image.ANTIALIAS)
my_img4 = ImageTk.PhotoImage(my_img4)

my_img5 = Image.open('images/5.jpg')
my_img5 = my_img5.resize((400, 600), Image.ANTIALIAS)
my_img5 = ImageTk.PhotoImage(my_img5)

my_img6 = Image.open('images/6.jpg')
my_img6 = my_img6.resize((400, 600), Image.ANTIALIAS)
my_img6 = ImageTk.PhotoImage(my_img6)

"""
Putting all images into a list so displaying images code will be easier to
put up together.
"""
image_list = [
    my_img1,
    my_img2,
    my_img3,
    my_img4,
    my_img5,
    my_img6
]

# Creating a label which will display images.
my_label = Label(image=my_img1)
# Displaying the label on the window.
my_label.grid(row=0, column=0, columnspan=3)

# A global variable representing an index of the image_list image.
index = 0


def change_image(change):
    """
    Displays images back and forth.
    :param change: char value ('b' -> backwards or 'f' -> forward)
    """
    global my_label
    global index

    """
    If we're going backwards and we don't go below the lowest index in the
    next step, the program will display the previous image.
    """
    if change == 'b' and index - 1 >= 0:
        # Remove the old image.
        my_label.grid_forget()
        # Decrease index by 1.
        index -= 1
        """
        Re-create the label displaying images and display the previous 
        image in the list.
        """
        my_label = Label(image=image_list[index])
        # Display the label on the window.
        my_label.grid(row=0, column=0, columnspan=3)

    """
    If we're going forwards and we don't go above the highest index in the 
    next step, the program will display the next image.
    """
    if change == 'f' and index + 1 < len(image_list):
        # Remove the old image.
        my_label.grid_forget()
        # Increase index by 1.
        index += 1
        """
        Re-create the label displaying images and display the next
        image in the list.
        """
        my_label = Label(image=image_list[index])
        # Display the label on the window.
        my_label.grid(row=0, column=0, columnspan=3)


# Creating buttons that will let user view images.
button_backward = Button(root, text='<<', padx=20, pady=20,
                         command=lambda: change_image('b'))
button_exit = Button(root, text='EXIT', padx=20, pady=20, command=root.quit)
button_forward = Button(root, text='>>', padx=20, pady=20,
                        command=lambda: change_image('f'))

# Putting buttons into the window.
button_backward.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

# The main program loop.
root.mainloop()
