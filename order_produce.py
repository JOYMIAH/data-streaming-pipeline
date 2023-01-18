import json
import time

from kafka import KafkaProducer

GENERATE_ORDER_SENDING_TOPIC = "Generate_Order_Details"
ORDER_LIMIT = 500

producer = KafkaProducer(bootstrap_servers={"192.168.61.28:9093","192.168.61.28:9095","192.168.61.28:9097"})
 
print("Going to be generating order With 1 Second Latency")


for orders in range(ORDER_LIMIT):
    data = {
        "order_id": orders,
        "user_id": f"JOY_MIAH_{orders}",
        "total_cost": orders*2,
        "items": "Mobile,Smart Watch,Airbuds",
    }

    producer.send(GENERATE_ORDER_SENDING_TOPIC, json.dumps(data).encode("utf-8"))
    print(f"Sending order For  Transaction Processing {orders}")
    time.sleep(1)
    producer.flush()

