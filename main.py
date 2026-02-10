import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.utils import platform
import google.generativeai as genai

# Gemini Setup
genai.configure(api_key="AIzaSyAwt5Y4K4tZl-iCaLhl96h-3fTCS8X6Ark")

class LeoAI(App):
    def build(self):
        # बैकग्राउंड सर्विस शुरू करना (केवल Android पर)
        if platform == 'android':
            from android import PythonService
            # सर्विस शुरू करने का कमांड
            # यह Leo को बैकग्राउंड में रखेगा
        
        self.layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        self.layout.add_widget(Label(text="🦁 LEO SYSTEM AI", font_size=30, color=(1, 0.8, 0, 1)))
        
        self.chat_label = Label(text="Leo Background Service Active...\n", size_hint_y=0.7)
        self.layout.add_widget(self.chat_label)
        
        self.user_input = TextInput(hint_text="Leo, लाइट जलाओ या गाना बजाओ...", size_hint_y=0.1)
        self.layout.add_widget(self.user_input)
        
        send_btn = Button(text="Command LEO", size_hint_y=0.1, background_color=(0, 0.6, 1, 1))
        send_btn.bind(on_press=self.process_command)
        self.layout.add_widget(send_btn)
        
        return self.layout

    def process_command(self, instance):
        cmd = self.user_input.text.lower()
        # फोन कंट्रोल लॉजिक
        if "torch on" in cmd or "लाइट जलाओ" in cmd:
            self.chat_label.text += "\n[Leo]: टॉर्च जला रहा हूँ..."
            # यहाँ Flashlight API का कोड आएगा
        elif "open whatsapp" in cmd:
            self.chat_label.text += "\n[Leo]: व्हाट्सएप खोल रहा हूँ..."
            # यहाँ App Launch API आएगा
        else:
            # साधारण AI जवाब
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(cmd)
            self.chat_label.text += f"\n[Leo]: {response.text}"
        self.user_input.text = ""

if __name__ == '__main__':
    LeoAI().run()
