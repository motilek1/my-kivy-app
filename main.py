import datetime
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.pickers import MDTimePicker
from plyer import notification

# Графічний інтерфейс програми
KV = '''
MDFloatLayout:

    MDTopAppBar:
        title: "Нагадувальник"
        pos_hint: {"top": 1}
        elevation: 4

    MDTextField:
        id: reminder_text
        hint_text: "Про що нагадати?"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint_x: 0.8

    MDRaisedButton:
        id: time_btn
        text: "Обрати час"
        pos_hint: {"center_x": 0.5, "center_y": 0.48}
        on_release: app.show_time_picker()

    MDFillRoundFlatButton:
        text: "Встановити нагадування"
        pos_hint: {"center_x": 0.5, "center_y": 0.35}
        on_release: app.set_reminder()
'''

class ReminderApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_time = None

    def build(self):
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_string(KV)

    def show_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_save=self.on_time_save)
        time_dialog.open()

    def on_time_save(self, instance, time_obj):
        self.selected_time = time_obj
        self.root.ids.time_btn.text = f"Час: {time_obj.strftime('%H:%M')}"

    def set_reminder(self):
        text = self.root.ids.reminder_text.text.strip()
        if not text:
            return

        # Відправка сповіщення у шторку Android
        notification.notify(
            title="Нагадування!",
            message=text,
            app_name="ReminderApp",
            timeout=10
        )

if __name__ == "__main__":
    ReminderApp().run()