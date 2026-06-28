[app]
title = My Application
package.name = fishfeeder
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[android]
# CRITICAL: These versions must match the pre-installed tools in your build.yml
android.api = 34
android.sdk_build_tools_version = 34.0.0
android.ndk = 25b
android.minapi = 21
android.archs = arm64-v8a

# Permissions
android.permissions = INTERNET

# This helps avoid issues with newer Android requirements
p4a.branch = master
