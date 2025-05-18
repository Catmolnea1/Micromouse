import requests

TOKEN = "PAST YOUR TOKEN"


class Mouse:

    def forward(self):
        response = requests.post(f'http://127.0.0.1:8801/api/v1/robot-cells/forward?token={TOKEN}')
        if response:
            return True
        else:
            return False

    def right(self):
        response = requests.post(f'http://127.0.0.1:8801/api/v1/robot-cells/right?token={TOKEN}')
        if response:
            return True
        else:
            return False

    def left(self):
        response = requests.post(f'http://127.0.0.1:8801/api/v1/robot-cells/left?token={TOKEN}')
        if response:
            return True
        else:
            return False

    def backward(self):
        response = requests.post(f'http://127.0.0.1:8801/api/v1/robot-cells/backward?token={TOKEN}')
        if response:
            return True
        else:
            return False





    def sensor(self):
        self.response = requests.get(f'http://127.0.0.1:8801/api/v1/robot-cells/sensor-data?token={TOKEN}').json()
        if self.response:
            return (True, self.response['front_distance'],
                    self.response['right_side_distance'],
                    self.response['back_distance'],
                    self.response['left_side_distance'],
                    self.response['rotation_yaw'])
        else:
            return False


