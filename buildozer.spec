[app]
title = Turkiye Kupasi
package.name = turkiyekupasi
package.domain = org.kupasimulasyon
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0.0

requirements = python3,kivy

orientation = portrait
fullscreen = 1
android.archs = arm64-v8a

android.api = 33
android.minapi = 21
android.ndk_api = 21
android.allow_backup = True
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
