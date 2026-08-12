[app]

# Назва програми на екрані телефона
title = Reminder App

# Системне ім'я
package.name = reminderapp
package.domain = org.test

# Всі файли коду в папці
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Версія вашої програми
version = 0.1

# Всі необхідні бібліотеки Python для Android
requirements = python3,kivy==2.3.0,kivymd==1.2.0,plyer,pillow,urllib3,certifi,idna,charset-normalizer

# Системні дозволи Android (для сповіщень та вібрації)
android.permissions = POST_NOTIFICATIONS, RECEIVE_BOOT_COMPLETED, VIBRATE

# Налаштування екрана
orientation = portrait
fullscreen = 0

# Версія Android SDK
android.api = 33
android.minapi = 21
android.ndk = 25b