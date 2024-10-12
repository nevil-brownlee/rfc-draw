# 1107, Mon 25 Sep 2023 (NZDT)
#
# test-font.py: Explore tkinter.font and tk.Text(.., font="TkFixedFont")
#
# Copyright 2023, Nevil Brownlee, Taupo NZ

import tkinter as tk
import tkinter.font

root = tk.Tk()  # Main window
root.title("RFC-draw")
root.geometry('800x600+5+5')
root.resizable(True, True)

d_canvas = tk.Canvas(root, width=600, height=250, bg="lightgrey",
    highlightthickness=0)
d_canvas.pack(expand=1)
d_canvas.message = tk.Frame(d_canvas, height=60, width=500,
    bg="azure")

d_canvas.message.place(x=50, y=50)
d_canvas.message.update()

s =  "123456789012345678901234567890\n"  # \n marks end of line
s2 = "         0         0         0"

fx_font = "TkFixedFont"  # This works (below) to set canvas.m_text !!!
#       = 'TkFixedFont 24"    doesn't work
#font = tkinter.font.Font(family="TkFixedFont")  # Can't set size here
#font = tkinter.font.Font(family="Droid Sans Mono")
#font = tkinter.font.Font(family="Nimbus Sans Mono", "size":12, weight)
font = tkinter.font.Font("family":"Noto Sans Mono")

d_canvas.m_text = tk.Text(d_canvas.message, fg="black", font=fx_font)
d_canvas.m_text.place(x=7, y=7)
d_canvas.m_text.delete('1.0', tk.END)
d_canvas.m_text.insert('1.0',  s)
d_canvas.m_text.update()
d_canvas.m_text.insert('2.0', s2)
d_canvas.m_text.update()

#!s_size = 17  # points (default)

print("actual returned %s" % font.actual())
   # > {'family': 'DejaVu Sans', 'size': 12, 'weight': 'normal', ...
   # > Clearly tkinter uses "DejaVu Sans 12" for TkFixedFont!

s_width = font.measure(s[0:-2])  # tk units, int
s_height = font.metrics("linespace")  # tk units, int

#print("width %s, len %s %s, size %s, height %s" % (
#    s_width, len(s)-1, type(s_width), s_size, s_height))
print("len %s, width %s (%s), height %s" % (
    len(s)-1, s_width, type(s_width), s_height))

c_width = float(s_width)/(len(s)-1)
print("s1 c_width %.3f %s" % (c_width, type(c_width)))
c_width = float(s_width)/(len(s2))
print("s2 c_width %.3f %s" % (c_width, type(c_width)))

print("waiting for input <<<")
input()