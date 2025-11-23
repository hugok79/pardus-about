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
            os.makedirs(
                "{}/{}/LC_MESSAGES".format(podir, po.split(".po")[0]), exist_ok=True
            )
            mo_file = "{}/{}/LC_MESSAGES/{}".format(
                podir, po.split(".po")[0], "pardus-about.mo"
            )
            msgfmt_cmd = "msgfmt {} -o {}".format(podir + "/" + po, mo_file)
            subprocess.call(msgfmt_cmd, shell=True)
            mo.append(
                (
                    "/usr/share/locale/" + po.split(".po")[0] + "/LC_MESSAGES",
                    ["po/" + po.split(".po")[0] + "/LC_MESSAGES/pardus-about.mo"],
                )
            )
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
    ("/usr/bin", ["pardus-about"]),
    ("/usr/share/applications", ["data/tr.org.pardus.python-gtk.desktop"]),
    ("/usr/share/pardus/pardus-about/ui", ["ui/MainWindow.glade"]),
    (
        "/usr/share/pardus/pardus-about/src",
        [
            "src/Main.py",
            "src/MainWindow.py",
            "src/UserSettings.py",
            "src/Actions.py",
            "src/__version__",
        ],
    ),
    (
        "/usr/share/pardus/pardus-about/data",
        [
            "data/style.css",
            "data/tr.org.pardus.python-gtk-autostart.desktop",
            "data/pardus-about.svg",
            "data/pardus-about-on-symbolic.svg",
            "data/pardus-about-off-symbolic.svg",
        ],
    ),
    (
        "/usr/share/icons/hicolor/scalable/apps/",
        [
            "data/assets/pardus-about.svg",
            "data/assets/pardus-about-symbolic.svg",
            "data/assets/pardus-hardware-info.svg",
            "data/assets/pardus-about-audio.svg",
            "data/assets/pardus-about-bluetooth.svg",
            "data/assets/pardus-about-camera.svg",
            "data/assets/pardus-about-computer.svg",
            "data/assets/pardus-about-desktop.svg",
            "data/assets/pardus-about-ethernet.svg",
            "data/assets/pardus-about-fingerprint.svg",
            "data/assets/pardus-about-graphics.svg",
            "data/assets/pardus-about-keyboard.svg",
            "data/assets/pardus-about-memory.svg",
            "data/assets/pardus-about-monitor.svg",
            "data/assets/pardus-about-mouse.svg",
            "data/assets/pardus-about-printer.svg",
            "data/assets/pardus-about-processor.svg",
            "data/assets/pardus-about-publicip.svg",
            "data/assets/pardus-about-storage.svg",
            "data/assets/pardus-about-touchpad.svg",
            "data/assets/pardus-about-wifi.svg",
            "data/assets/pardus-about-bios.svg",
            "data/assets/pardus-about-main.svg",
            "data/assets/pardus-about-network-card.svg"
        ],
    ),
] + create_mo_files()

setup(
    name="pardus-about",
    version=version,
    packages=find_packages(),
    scripts=["pardus-about"],
    install_requires=["PyGObject"],
    data_files=data_files,
    author="Mehmet Zahid Berktas",
    author_email="mehmet.berktas@tubitak.gov.tr",
    description="Pardus About Application",
    license="GPLv3",
    keywords="pardus-about, pardus-hardware-info",
    url="https://github.com/pardus/pardus-about",
)
