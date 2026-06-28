import json
import os
from datetime import datetime
from kivy.app import App
from kivy.clock import Clock

class FishFeederApp(App):
    DATA_FILE = "feed_log.json"

    def build(self):
        # Schedule: Check clock every 60 seconds, check sensor every 5 seconds
        Clock.schedule_interval(self.check_autopilot, 60)
        Clock.schedule_interval(self.read_sensor, 5)
        # Note: No 'return' needed; Kivy auto-loads fishfeeder.kv
    
    def load_data(self):
        if os.path.exists(self.DATA_FILE):
            with open(self.DATA_FILE, 'r') as f:
                return json.load(f)
        return {"manual_feeds": 0, "last_date": ""}

    def save_data(self, data):
        with open(self.DATA_FILE, 'w') as f:
            json.dump(data, f)

    def feed_fish(self, passcode):
        data = self.load_data()
        today = datetime.now().strftime("%Y-%m-%d")

        # Reset count if it's a new day
        if data["last_date"] != today:
            data["manual_feeds"] = 0
            data["last_date"] = today

        # Check logic: < 2 manual feeds OR valid passcode
        if data["manual_feeds"] < 2 or passcode == "9876":
            self.root.ids.status_label.text = "Status: Feeding..."
            # --- INSERT MOTOR ACTIVATION CODE HERE ---
            print("Motor Activated!")
            
            # Increment and save
            data["manual_feeds"] += 1
            self.save_data(data)
        else:
            self.root.ids.status_label.text = "Status: LIMIT REACHED"

    def check_autopilot(self, dt):
        now = datetime.now()
        # Trigger at 00:00 (Midnight) or 12:00 (Noon)
        if (now.hour == 0 or now.hour == 12) and now.minute == 0:
            self.root.ids.status_label.text = "Status: AUTOPILOT ACTIVE"
            # --- INSERT MOTOR ACTIVATION CODE HERE ---
            print("Autopilot Feeding!")

    def read_sensor(self, dt):
        # Stub for your sensor logic
        try:
            # Replace with actual sensor read
            distance = 15 
            self.root.ids.dist_label.text = f"Distance: {distance} cm"
        except Exception as e:
            self.root.ids.dist_label.text = "Sensor Error"

if __name__ == '__main__':
    FishFeederApp().run()
