[app]
title = Fizrenkli
package.name = fizrenkli
package.domain = org.example
source.dir = .
source.main = fizrenkli.py
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.archs = arm64-v8a,armeabi-v7a
