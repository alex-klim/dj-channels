from channels.routing import route

from chat.consumers import ws_disconnect, ws_add, ws_message

channel_routing = [
    route("websocket.receive", ws_message),
    route('websocket.connect', ws_add),
    route('websocket.disconnect', ws_disconnect),
]
