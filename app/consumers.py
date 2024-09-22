import json

from channels.generic.websocket import JsonWebsocketConsumer


class LiveblogConsumer(JsonWebsocketConsumer):
    groups = ["liveblog"]

    def liveblog_post_created(self, event_dict):
        self.send_json(event_dict)

    def liveblog_post_updated(self, event_dict):
        self.send_json(event_dict)

    def liveblog_post_deleted(self, event_dict):
        self.send_json(event_dict)


class EchoConsumer(JsonWebsocketConsumer):
    '''
    웹소켓 클라이언트에서 text_frame으로 보내면, text data 인자에 담겨 호출
    binary frame에 담아 보내면 bytes data 에 담겨 호출된다
    ref: javascript websocket
    '''
    def receive(self, content=None, **kwargs):
        print(f"수신: {content}")
        self.send_json({
            "content": content["content"],
            "user": content["user"]
        })
        # self.send(f"You said: {text_data}")
