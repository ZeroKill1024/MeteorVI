#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import platform
import shutil

if __name__ == "__main__":
    print("**********begin install...**********")
    sources = "Sources/"
    destPath = os.environ["HOME"] + '/'
    if (platform.system() == "Windows"):
        destPath = os.environ["VIM"] + '/'
    print("copy files from " + sources + ':')
    if os.path.exists(sources) and os.path.isdir(sources):
        for path, dirs, files in os.walk(sources):
            for f in files:
                relPath = os.path.join(path, f)
                print(relPath)
                if (platform.system() != "Windows"):
                    f = f.replace('_', '.')
                shutil.copy(relPath, destPath + f)
    print("to " + destPath)

    runtime = "Runtime/vimfiles"
    if (platform.system() == "Windows"):
        destPath += "vimfiles/"
    else:
        destPath += ".vim/"
    print("copy files from " + runtime + ':')
    if os.path.exists(runtime) and os.path.isdir(runtime):
        for path, dirs, files in os.walk(runtime):
            for f in files:
                relPath = os.path.join(path, f)
                newPath = destPath + path.split('/')[-1] + '/'
                print(relPath)
                if not os.path.exists(newPath):
                    os.mkdir(newPath)
                shutil.copy(relPath, newPath + f)
    print("to " + destPath)
    print("**********install successful**********")
