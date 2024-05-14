import pika

def on_message_recived(ch, method, properties, body):
    print(f"recived new message: {body}")

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue = 'hello')

channel.basic_consume(queue= 'hello', auto_ack=True,
                      on_message_callback= on_message_recived )

print("Starting consuming")

channel.start_consuming()
