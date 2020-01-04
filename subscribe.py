import paho.mqtt.client as mqtt

config = {
    'address': 'my-address',
    'port': 1883,
    'username': 'mqtt-test',
    'password': 'mqtt-test'
}


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("#")


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    # client.tls_set()
    # client.tls_insecure_set(True)
    client.username_pw_set(config['username'], config['password'])
    client.connect(config['address'], config['port'], 60)
    client.loop_forever()
