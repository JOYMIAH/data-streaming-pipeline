from kafka import KafkaConsumer
CONFIRMED_ORDER_SENDING_TOPIC = "Generate_Order_Details"
consumer = KafkaConsumer(CONFIRMED_ORDER_SENDING_TOPIC ,bootstrap_servers={"192.168.61.28:9093","192.168.61.28:9095","192.168.61.28:9097"},
auto_offset_reset='earliest'
# group_id='Consumer-Group-2'
)

print("Start Acquiring All  Confirmed Order Data")
while True:
    for message in consumer:
        print("Here is a message..")
        print (message)
