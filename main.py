import datetime
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

# ==========================================
# 1. YOUR KV LAYOUT DESIGN (The Visuals)
# ==========================================
KV = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDBoxLayout:
        orientation: 'vertical'
        padding: "16dp"
        spacing: "20dp"

        # App Header
        MDLabel:
            text: "Smart Fish Feeder"
            halign: "center"
            font_style: "Display"
            role: "small"
            bold: True
            size_hint_y: None
            height: "60dp"

        # Status Card
        MDCard:
            orientation: "vertical"
            padding: "16dp"
            size_hint: (1, None)
            height: "140dp"
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
                
                MDLabel:
                    id: log_label
                    text: " App started successfully.\\n Waiting for manual feed command..."
                    font_style: "Body"
                    role: "small"
                    halign: "left"
                    valign: "top"

        # Action Area (The Button)
        MDBoxLayout:
            size_hint_y: None
            height: "80dp"
            anchor_x: "center"
            anchor_y: "center"
            
            MDButton:
                style: "filled"
                size_hint_x: .8
                pos_hint: {"center_x": .5}
                on_release: app.trigger_feeding()
                
                MDButtonText:
                    text: "FEED NOW"
                    pos_hint: {"center_x": .5, "center_y": .5}
'''

# ==========================================
# 2. YOUR PYTHON LOGIC (The Brains)
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
        This function handles the action when the 'FEED NOW' button is pressed.
        It updates the UI labels dynamically.
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
