import psutil
import time
import threading

def monitor_bandwidth(interval=1):
    last_bytes_sent = psutil.net_io_counters().bytes_sent
    last_bytes_recv = psutil.net_io_counters().bytes_recv

    while True:
        time.sleep(interval)
        bytes_sent = psutil.net_io_counters().bytes_sent - last_bytes_sent
        bytes_recv = psutil.net_io_counters().bytes_recv - last_bytes_recv
        mb_sent = bytes_sent / (1024 * 1024)
        mb_recv = bytes_recv / (1024 * 1024)

        # Stocker les statistiques de bande passante dans une variable globale
        bandwidth_stats = {'sent': mb_sent, 'recv': mb_recv}
        yield bandwidth_stats

        last_bytes_sent = psutil.net_io_counters().bytes_sent
        last_bytes_recv = psutil.net_io_counters().bytes_recv

def start_bandwidth_monitor(interval=1):
    # Démarrer la surveillance de la bande passante dans un thread séparé
    bandwidth_thread = threading.Thread(target=monitor_bandwidth, args=(interval,))
    bandwidth_thread.daemon = True
    bandwidth_thread.start()
