import datetime

# =========================================================================
# 1. FORCE 9:16 RATIO (Must happen BEFORE any other Kivy/KivyMD imports)
# =========================================================================
from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', '0')  # Locks the window to 9:16 ratio

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

# ==========================================
# 2. YOUR KV LAYOUT DESIGN (The Visuals)
# ==========================================
KV = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDBoxLayout:
        orientation: 'vertical'
        padding: "16dp"
        spacing: "16dp"

        # App Header
        MDLabel:
            text: "Smart Fish Feeder"
            halign: "center"
            font_style: "Display"
            role: "small"
            bold: True
            size_hint_y: None
            height: "50dp"

        # Status Card
        MDCard:
            orientation: "vertical"
            padding: "16dp"
            size_hint: (1, None)
            height: "130dp"
            style: "elevated"
            theme_bg_color: "Custom"
            md_bg_color: self.theme_cls.surfaceContainerLowColor
            radius: [16, 16, 16, 16]

            MDLabel:
                text: "FEEDER STATUS"
                font_style: "Label"
                role: "large"
                theme_text_color: "Secondary"
            
            MDLabel:
                id: status_label
                text: "Status: Ready"
                font_style: "Headline"
                role: "medium"
                bold: True
            
            MDLabel:
                id: last_fed_label
                text: "Last Feeding: Not fed yet today"
                font_style: "Body"
                role: "medium"
                theme_text_color: "Secondary"

        # History Log Section
        MDBoxLayout:
            orientation: "vertical"
            spacing: "8dp"
            size_hint_y: 1  # Takes up all remaining vertical space dynamically
            
            MDLabel:
                text: "Activity Log"
                font_style: "Title"
                role: "medium"
                bold: True
                size_hint_y: None
                height: "30dp"
                
            MDCard:
                padding: "12dp"
                style: "outlined"
                size_hint_y: 1
                
                MDLabel:
                    id: log_label
                    text: " App started successfully.\\n Waiting for manual feed command..."
                    font_style: "Body"
                    role: "small"
                    halign: "left"
                    valign: "top"
                    text_size: self.width, None

        # Action Area (The Button)
        MDBoxLayout:
            size_hint_y: None
            height: "70dp"
            anchor_x: "center"
            anchor_y: "center"
            
            MDButton:
                style: "filled"
                size_hint_x: .9
                pos_hint: {"center_x": .5}
                on_release: app.trigger_feeding()
                
                MDButtonText:
                    text: "FEED NOW"
                    pos_hint: {"center_x": .5, "center_y": .5}
'''

# ==========================================
# 3. YOUR PYTHON LOGIC (The Brains)
# ==========================================
class FishFeederApp(MDApp):
    def build(self):
        # Configure App Theme
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        
        # Load the combined string from above
        return Builder.load_string(KV)

    def trigger_feeding(self):
        """
        Handles the action when the 'FEED NOW' button is pressed.
        Updates the UI labels dynamically.
        """
        # Get current time stamp
        now = datetime.datetime.now().strftime("%I:%M:%S %p")
        
        # Update the labels inside the layout using their IDs
        self.root.ids.status_label.text = "Status: Feeding Dispensed!"
        self.root.ids.last_fed_label.text = f"Last Feeding: Today at {now}"
        
        # Append to the history log
        current_log = self.root.ids.log_label.text
        new_entry = f"\\n [{now}] Manual feeding sequence activated successfully."
        self.root.ids.log_label.text = current_log + new_entry


if __name__ == '__main__':
    # Launch the application
    FishFeederApp().run()
