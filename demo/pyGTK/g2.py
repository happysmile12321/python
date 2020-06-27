#!/usr/bin/env python
# Created by xiaosanyu at 16/6/13
# section 005
TITLE = "Properties"
DESCRIPTION = """
Properties describe the configuration and state of widgets
"""
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class PyApp(Gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__(title="Properties")
        self.set_size_request(200, 100)
        self.label = Gtk.Label(label="Hello World",
                               angle=25,
                               halign=Gtk.Align.END)
        print(self.label.props.label)
        self.label.props.label = "New word"
        print(self.label.get_property("label"))
        self.label.set_property("label", "Hello World!!!")

        self.add(self.label)
        print(dir(self.label.props))


def main():
    win = PyApp()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()


if __name__ == "__main__":
    main()
