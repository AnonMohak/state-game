#to get the x and y coordinates of screen onclick.
#you can also loop around and save in a list which can later be turned into pandas database together with state names.

import turtle as tu
screen = tu.Screen()
image = 'states.gif'
screen.addshape(image)

tu.shape(image)
def get_mouse_click_coor(x, y):
    print(x, y)

tu.onscreenclick(get_mouse_click_coor)

tu.mainloop()