import random
import json
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

class TurkiyeKupasiApp(App):
    def build(self):
        Window.clearcolor = (0.12, 0.12, 0.12, 1)
        
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        title = Label(
            text="🏆 TÜRKİYE KUPASI SİMÜLASYONU 🏆",
            font_size='22sp',
            bold=True,
            size_hint_y=None,
            height=60,
            color=(1, 0.84, 0, 1)
        )
        main_layout.add_widget(title)
        
        scroll = ScrollView()
        self.content_grid = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.content_grid.bind(minimum_height=self.content_grid.setter('height'))
        
        welcome_text = (
            "Türkiye Kupası Simülasyonuna Hoş Geldiniz!\n\n"
            "Turnuva mantığınız ve kupa eşleşmeleriniz bu ekran üzerinde\n"
            "mobil uyumlu butonlar ve tablolarla listelenecektir.\n\n"
            "APK kurulumunuz başarıyla tamamlanmıştır."
        )
        self.info_label = Label(
            text=welcome_text,
            font_size='15sp',
            halign='center',
            valign='middle',
            size_hint_y=None,
            height=200
        )
        self.content_grid.add_widget(self.info_label)
        scroll.add_widget(self.content_grid)
        main_layout.add_widget(scroll)
        
        self.action_btn = Button(
            text="Turnuvayı Başlat",
            font_size='18sp',
            bold=True,
            size_hint_y=None,
            height=60,
            background_color=(0, 0.6, 0.2, 1)
        )
        main_layout.add_widget(self.action_btn)
        
        return main_layout

if __name__ == '__main__':
    TurkiyeKupasiApp().run()
  
