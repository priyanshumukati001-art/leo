[app]
title = LEO AI
package.name = leoai
package.domain = org.leo
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 2.5
requirements = python3,kivy,google-generativeai,requests,urllib3,certifi,chardet,idna
orientation = portrait
permissions = INTERNET, RECORD_AUDIO, FOREGROUND_SERVICE, CAMERA, CALL_PHONE
services = LeoService:service.py
android.archs = arm64-v8a
