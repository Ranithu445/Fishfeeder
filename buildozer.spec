[app]

# (str) Title of your application
title = fishfeeder

# (str) Package name
package.name = Fishfeeder

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let everything default to all, or list specific)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Add your libraries here (e.g., requests, pillow, etc.)
requirements = python3,kivy

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage
build_dir = .buildozer

# !!! CRITICAL FOR GITHUB ACTIONS !!!
# This tells the build server to automatically accept the license 
# without you needing to type "y" in a terminal.
android.accept_sdk_license = True