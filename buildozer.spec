[app]
title = Fizrenkli
package.name = fizrenkli
package.domain = org.kicijikshazada
source.dir = .
source.main = fizrenkli.py
version = 0.2
requirements = python3,kivy
orientation = portrait
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.archs = arm64-v8a,armeabi-v7a
android.build_tools = 30.0.3
