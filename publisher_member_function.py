import rclpy
from rclpy.node import Node

from std_msgs.msg import String
# Serial communication
import serial
arduinoDaten = serial.Serial('/dev/ttyACM0',9600)

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.subscription = self.create_subscription( # From subscription example
            String,
            'led_steuerung',
            self.listener_callback,
            10
        )
        self.get_logger().info("serieller Knoten initialisiert")

        while True:
            meinBefehl = input('Bitte geben Sie Ihren Befehl ein: ')
            meinBefehl = meinBefehl + '\r'
            arduinoDaten.write(meinBefehl.encode())

    def listener_callback(self, msg):
        self.get_logger().info("Befehl senden: %s" % msg.data)

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
