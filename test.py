# import pyglet

# animation = pyglet.image.load_animation('gg.gif')
# animSprite = pyglet.sprite.Sprite(animation)

# w = animSprite.width
# h = animSprite.height

# window = pyglet.window.Window(width=w, height=h)
# # r, g, b, alpha = 0.5, 0.5, 0.8, 0.5
# # pyglet.gl.glClearColor(r, g, b, alpha)


# @window.event
# def on_draw():
#     window.clear()
#     animSprite.draw()


# pyglet.app.run()

from tkinter import *
import time
import os
root = Tk()

frames = [PhotoImage(file='gg.gif',
                     format='gif -index %i' % (i)) for i in range(100)]


def update(ind):
    frame = frames[ind]
    ind += 1
    label.configure(image=frame)
    root.after(10, update, ind)


label = Label(root)
label.pack()
root.after(0, update, 0)
root.mainloop()
