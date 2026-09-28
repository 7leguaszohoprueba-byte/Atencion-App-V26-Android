[app]
# Atención V26 - Android
# Proyecto de compilación de la versión Android.
title = Atención V26
package.name = atencionv26
package.domain = mx.atencion
source.dir = app
source.include_exts = py,png,jpg,kv,atlas,xlsx,txt
version = 26.0
requirements = python3,kivy,requests,openpyxl,pyjnius
orientation = portrait
fullscreen = 0
android.api = 35
android.minapi = 23
android.archs = arm64-v8a,armeabi-v7a
android.permissions = INTERNET
android.allow_backup = True
android.debug_artifact = apk
android.release_artifact = aab

[buildozer]
log_level = 2
warn_on_root = 1

[graphics]
# Kivy usa SDL2 y adapta los controles a la pantalla táctil.
