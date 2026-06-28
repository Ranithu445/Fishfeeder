[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# Add your other dependencies here (e.g., requests, pillow)
requirements = python3,kivy

# (str) Presplash of the application
# (str) Icon of the application
# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET

# (int) Android API to use (34 is stable for this build)
android.api = 34

# (int) Minimum API required (21 is standard for modern devices)
android.minapi = 21

# (str) Android SDK Build-Tools version (Locked to 34.0.0)
android.sdk_build_tools_version = 34.0.0

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir (False)
android.private_storage = True

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

[buildozer]
# (int) Log level (0 = error, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
