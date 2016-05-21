import logging


class RobotHandler(logging.Handler):

    def __init__(self, access_token, room_name, endpoint='https://api.hipchat.com'):
        logging.Handler.__init__(self)

# https://docs.python.org/2/howto/logging.html#configuring-logging-for-a-library
# Good example: https://github.com/invernizzi/hiplogging/blob/master/hiplogging/__init__.py
