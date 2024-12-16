import paho.mqtt.client as mqtt
import requests

# Define the callback function for when the connection is successful
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribe to a topic after connecting
    client.subscribe("alert")

# Define the callback function for when a message is received
def on_message(client, userdata, msg):
    message = {'message': msg.payload.decode()}
    base_url = f"http://185.105.187.116:7008/api/v1/push/broadcast/alert"
    response = requests.post(base_url, json=message)

    print(f"Message received: {msg.payload.decode()}")


# Create a new MQTT client
client = mqtt.Client()

# Set the username and password for authentication
client.username_pw_set("user1", "nzstwz98")

# Set the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker (replace with your broker address)
client.connect("185.105.187.115", 1883, 60)

# Start the MQTT client loop to listen for messages
client.loop_forever()
