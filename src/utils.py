
import psutil
import time

def flatten_dict(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

def get_cpu_usage():
    return psutil.cpu_percent()

def get_memory_usage():
    return psutil.virtual_memory().percent

def get_network_usage():
    io1 = psutil.net_io_counters()
    time.sleep(1)
    io2 = psutil.net_io_counters()

    bytes_sent_per_sec = (io2.bytes_sent - io1.bytes_sent) / 1.0 
    bytes_recv_per_sec = (io2.bytes_recv - io1.bytes_recv) / 1.0 

    return bytes_recv_per_sec, bytes_sent_per_sec
