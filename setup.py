#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# This file is template/test 
# 

import os
import subprocess

from setuptools import setup, find_packages


def create_mo_files():
    podir = "po"
    mo = []
    for po in os.listdir(podir):
        if po.endswith(".po"):
            os.makedirs("{}/{}/LC_MESSAGES".format(podir, po.split(".po")[0]), exist_ok=True)
            mo_file = "{}/{}/LC_MESSAGES/{}".format(podir, po.split(".po")[0], "pardus-python-gtk.mo")
            msgfmt_cmd = 'msgfmt {} -o {}'.format(podir + "/" + po, mo_file)
            subprocess.call(msgfmt_cmd, shell=True)
            mo.append(("/usr/share/locale/" + po.split(".po")[0] + "/LC_MESSAGES",
                       ["po/" + po.split(".po")[0] + "/LC_MESSAGES/pardus-python-gtk.mo"]))
    return mo


changelog = "debian/changelog"
if os.path.exists(changelog):
    head = open(changelog).readline()
    try:
        version = head.split("(")[1].split(")")[0]
    except:
        print("debian/changelog format is wrong for get version")
        version = "0.0.0"
    f = open("src/__version__", "w")
    f.write(version)
    f.close()

data_files = [
    ("/usr/bin", ["pardus-python-gtk"]),
    ("/usr/share/applications",
     ["data/tr.org.pardus.python-gtk.desktop"]),
    ("/usr/share/pardus/pardus-python-gtk/ui",
     ["ui/MainWindow.glade"]),
    ("/usr/share/pardus/pardus-python-gtk/src",
     ["src/Main.py",
      "src/MainWindow.py",
      "src/UserSettings.py",
      "src/__version__"]),
    ("/usr/share/pardus/pardus-python-gtk/data",
     ["data/style.css",
      "data/tr.org.pardus.python-gtk-autostart.desktop",
      "data/pardus-python-gtk.svg",
      "data/pardus-python-gtk-on-symbolic.svg",
      "data/pardus-python-gtk-off-symbolic.svg"]),
    ("/usr/share/icons/hicolor/scalable/apps/",
     ["data/pardus-python-gtk.svg",
      "data/pardus-python-gtk-on-symbolic.svg",
      "data/pardus-python-gtk-off-symbolic.svg"])
] + create_mo_files()

setup(
    name="pardus-python-gtk",
    version=version,
    packages=find_packages(),
    scripts=["pardus-python-gtk"],
    install_requires=["PyGObject"],
    data_files=data_files,
    author="Yusuf Düzgün",
    author_email="yusuf.duzgun@pardus.org.tr",
    description="Pardus Python GTK EXAMPLE",
    license="GPLv3",
    keywords="pardus-python-gtk, example, test",
    url="https://github.com/pardus/pardus-python-gtk",
)
