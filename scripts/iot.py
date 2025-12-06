import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(msg.topic, msg.payload)

def load_iot():
    client = mqtt.Client()
    client.connect("broker.hivemq.com", 1883)
    client.subscribe("iot/sensor")
    client.on_message = on_message
    client.loop_start()
    return client

if __name__ == "__main__":
    load_iot()
