[app]

# (str) आपके ऐप का नाम
title = Leo AI

# (str) पैकेज का नाम
package.name = leoai

# (str) डोमेन नाम
package.domain = org.leo

# (str) सोर्स कोड की लोकेशन
source.dir = .

# (list) कौन-कौन सी फाइलें शामिल करनी हैं
source.include_exts = py,png,jpg,kv,atlas

# (str) ऐप का वर्शन
version = 1.0

# (list) सबसे महत्वपूर्ण: ये लाइब्रेरीज़ एरर नहीं देंगी
requirements = python3, kivy==2.2.1, google-generativeai, requests, certifi, urllib3, charset-normalizer, idna

# (str) ओरिएंटेशन
orientation = portrait

# (list) इंटरनेट परमिशन (AI के लिए ज़रूरी)
android.permissions = INTERNET

# (int) एंड्रॉइड API लेवल (31 सबसे स्टेबल है GitHub के लिए)
android.api = 31

# (int) कम से कम एंड्रॉइड वर्शन
android.minapi = 21

# (list) आर्किटेक्चर (सिर्फ ये दो रखें ताकि बिल्ड जल्दी हो)
android.archs = arm64-v8a, armeabi-v7a

# (bool) क्या ऐप फुल स्क्रीन होगा
fullscreen = 0

# (bool) लाइसेंस खुद स्वीकार करना (बिल्ड रोकने से बचाने के लिए)
android.accept_sdk_license = True

[buildozer]
# (int) लॉग लेवल (ताकि एरर साफ़ दिखे)
log_level = 2

# (int) वार्निंग ऑन रूट
warn_on_root = 1
