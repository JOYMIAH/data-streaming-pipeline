from kafka import KafkaConsumer
CONFIRMED_ORDER_SENDING_TOPIC = "test"
consumer = KafkaConsumer(CONFIRMED_ORDER_SENDING_TOPIC ,bootstrap_servers={'192.168.61.28:9093'},
auto_offset_reset='earliest'
# group_id='Consumer-Group-2'
)

print("Start Acquiring All  Confirmed Order Data")
while True:
    for message in consumer:
        print("Here is a message..")
        print (message)