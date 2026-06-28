[app]
title = Fishfeeder Control Panel
package.name = fishfeeder
package.domain = com.fishfeeder.app
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
# Added kivymd to requirements
requirements = python3,kivy,kivymd
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 34
android.sdk_build_tools_version = 34.0.0
android.ndk = 25b
android.minapi = 21
android.archs = arm64-v8a
android.permissions = INTERNET
p4a.branch = master
