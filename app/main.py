from fastapi import FastAPI
import psutil

app = FastAPI()

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.get('/cpu')
def cpu():
    return {'percent': psutil.cpu_percent(interval=0.1)}

@app.get('/memory')
def memory():
    mem = psutil.virtual_memory()
    return {'total': mem.total, 'available': mem.available, 'percent': mem.percent}

@app.get('/disk')
def disk():
    d = psutil.disk_usage('/')
    return {'total': d.total, 'used': d.used, 'free': d.free, 'percent': d.percent}

@app.get('/system')
def system():
    return {
        'platform': psutil.SYSTEM,
        'boot_time': psutil.boot_time()
    }

@app.get('/network')
def network():
    net = psutil.net_io_counters()
    return {
        'bytes_sent': net.bytes_sent,
        'bytes_recv': net.bytes_recv,
        'packets_sent': net.packets_sent,
        'packets_recv': net.packets_recv
    }
