import pika


class Messenger(object):
    def toggle_lights(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='aurora')
        channel.basic_publish(exchange='',
                              routing_key='aurora',
                              body='Toggle lights')
        connection.close()
