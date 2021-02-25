import pika
# helps in sending events


params = pika.URLParameters(

connection=pika.BlockingConnection(params)

channel=connection.channel()

channel.queue_declare(queue="admin")


def callback(channel, method, properties, body):
    print("Recieved in admin")
    print(body)


channel.basic_consume(
    queue="admin", on_message_callback=callback, auto_ack=True)

print("Started Consumening")

channel.start_consuming()

channel.close()
