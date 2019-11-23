import datetime

class Timer(object):
    """A simple timer class"""
    
    def __init__(self):
        pass
        self.pause_total = datetime.datetime.now() - datetime.datetime.now()
    
    def start(self):
        """Starts the timer"""
        self.start = datetime.datetime.now()
        return self.start
    
    def stop(self, message="Total: "):
        """Stops the timer.  Returns the time elapsed"""
        self.stop = datetime.datetime.now()
        return str((self.stop - self.start) - self.pause_total)
    
    def pause(self, message="Paused."):
        """Pauses the timer."""
        self.pause_start = datetime.datetime.now()
    
    def unpause(self, message="Unpaused."):
        """Unpauses timer."""
        self.pause_total = (datetime.datetime.now() - self.pause_start) + self.pause_total
        return datetime.datetime.now() - pause_start

    def now(self, message="Now: "):
        """Returns the current time with a message"""
        return message + ": " + str(datetime.datetime.now())
    
    def elapsed(self, message="Elapsed: "):
        """Time elapsed since start was called"""
        return message + str(datetime.datetime.now() - self.start)
    
    def split(self, message="Split started at: "):
        """Start a split timer"""
        self.split_start = datetime.datetime.now()
        return message + str(self.split_start)
    
    def unsplit(self, message="Unsplit: "):
        """Stops a split. Returns the time elapsed since split was called"""
        return message + str(datetime.datetime.now() - self.split_start)