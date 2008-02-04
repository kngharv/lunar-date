#!/usr/bin/python
import sys
import string
import gtk
import gclcalendar

def main_quit(object, *args):
	gtk.main_quit()

if __name__ == '__main__':
	window = gtk.Window()
	window.connect("delete-event", main_quit)

        cal = gclcalendar.Calendar()
        cal.set_display_options("show-lunar")
        window.add(cal)
	window.show_all()
	gtk.main()