#!/usr/bin/env python
# 名字变了，目前gtk只支持python2
# pip install PyGObject --user
# import gi
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
window = Gtk.Window(title="Hello,gtk")
window.show()
window.connect("destroy", Gtk.main_quit)
Gtk.main()
