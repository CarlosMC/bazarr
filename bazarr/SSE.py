from __future__ import absolute_import
from collections import deque
import json
import time


class EventStream:
    """
    This class is used to read or write items to the notifications deque.
    """
    
    def __init__(self):
        self.queue = deque(maxlen=100)
    
    def write(self, type=None, action=None, series=None, episode=None, movie=None):
        """
            :param type: The type of element.
            :type type: str
            :param action: The action type of element from insert, update, delete.
            :type action: str
            :param series: The series id.
            :type series: str
            :param episode: The episode id.
            :type episode: str
            :param movie: The movie id.
            :type movie: str
        """
        msg = {"type": type, "action": action, "series": series, "episode": episode, "movie": movie}
        self.queue.append("retry: 1000\ndata:" + json.dumps(msg) + "\n\n")
    
    def read(self):
        """
            :return: Return the oldest notification available.
            :rtype: str
        """

        while True:
            if self.queue:
                return self.queue.popleft()
            else:
                return ':'
            time.sleep(0.1)


event_stream = EventStream()
