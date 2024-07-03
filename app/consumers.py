import json

from channels.generic.websocket import WebsocketConsumer


class EchoConsumer(WebsocketConsumer):
    '''
    웹소켓 클라이언트에서 text_frame으로 보내면, text data 인자에 담겨 호출
    binary frame에 담아 보내면 bytes data 에 담겨 호출된다
    ref: javascript websocket
    '''
    def receive(self, text_data=None, bytes_data=None):
        obj = json.loads(text_data)
        print(f"수신: {obj}")

        json_string = json.dumps({
            "content": obj["content"],
            "user": obj["user"]
        })
        self.send(json_string)
        # self.send(f"You said: {text_data}")
