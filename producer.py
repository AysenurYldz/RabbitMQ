import pika

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue = "hello")

message = "Hi, this is my first message"

channel.basic_publish(exchange= '', routing_key= 'hello', body=message)

print(f"send message message: {message}")

connection.close()