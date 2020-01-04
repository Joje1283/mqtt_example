from time import sleep
import paho.mqtt.client as paho

config = {
    'address': 'my-address',
    'port': 1883,
    'username': 'mqtt-test',
    'password': 'mqtt-test'
}

topic = '/test/'

if __name__ == '__main__':
    client = paho.Client("client-001")
    client.username_pw_set(config['username'], config['password'])
    client.connect(config['address'], config['port'], 60)
    client.publish(topic, 'hello world', qos=1)
    sleep(1)
    client.disconnect()