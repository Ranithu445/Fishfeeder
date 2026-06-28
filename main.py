from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivy.core.window import Window
from kivy.clock import Clock
import time

# For desktop testing, simulates a mobile aspect ratio
Window.size = (360, 640)

class FishFeederApp(MDApp):
    def build(self):
        # 1. Professional Theme Configuration
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        
        # 2. Main Screen Layout
        screen = MDScreen()
        
        # 3. Main Container Card (The "Pro" Look)
        self.card = MDCard(
            size_hint=(0.9, 0.8),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            elevation=10,
            padding="20dp",
            spacing="15dp",
            orientation="vertical"
        )
        
        # 4. UI Elements
        self.lbl_title = MDLabel(
            text="SMART FISH FEEDER",
            halign="center",
            font_style="H5",
            theme_text_color="Primary"
        )
        
        self.lbl_time = MDLabel(
            text="00:00:00",
            halign="center",
            font_style="H4",
            theme_text_color="Custom",
            text_color=(0, 1, 1, 1) # Cyan color
        )
        
        self.lbl_sensor = MDLabel(
            text="Distance: -- cm",
            halign="center",
            theme_text_color="Secondary"
        )
        
        # 5. Feed Button
        self.btn_feed = MDRaisedButton(
            text="FEED NOW",
            pos_hint={"center_x": 0.5},
            size_hint=(0.6, 0.1)
        )
        self.btn_feed.bind(on_release=self.feed_action)
        
        # 6. Assemble
        self.card.add_widget(self.lbl_title)
        self.card.add_widget(self.lbl_time)
        self.card.add_widget(self.lbl_sensor)
        self.card.add_widget(self.btn_feed)
        screen.add_widget(self.card)
        
        # 7. Start the background clock
        Clock.schedule_interval(self.update_ui, 1)
        
        return screen

    def update_ui(self, dt):
        # Update Time
        self.lbl_time.text = time.strftime("%H:%M:%S")
        
        # Add your hardware sensor logic here!
        # Example: self.lbl_sensor.text = f"Distance: {get_sensor_value()} cm"

    def feed_action(self, instance):
        # Trigger your physical hardware/relay here
        print("Feeding sequence initiated!")
        self.lbl_title.text = "FEEDING..."
        # Reset text after 2 seconds
        Clock.schedule_once(lambda dt: setattr(self.lbl_title, 'text', "SMART FISH FEEDER"), 2)

if __name__ == '__main__':
    FishFeederApp().run()
