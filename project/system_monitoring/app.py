# import psutil
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def index():
#     cpu_percent = psutil.cpu_percent(interval=0.5)
#     mem_percent = psutil.virtual_memory().percent
#     message = None
#     if cpu_percent > 80 or mem_percent > 80:
#         message = "High CPU or memory utilization detected!"
#     return render_template("index.html", cpu_percent=cpu_percent, mem_percent=mem_percent, message=message)

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0',port=5001)


# import time
# import subprocess
# import psutil
# from flask import Flask, render_template, jsonify

# app = Flask(__name__)


# def get_gpu_stats():
#     try:
#         result = subprocess.run(
#             [
#                 'nvidia-smi',
#                 '--query-gpu=utilization.gpu,temperature.gpu',
#                 '--format=csv,noheader,nounits'
#             ],
#             capture_output=True, text=True, timeout=3
#         )
#         if result.returncode == 0:
#             parts = result.stdout.strip().split(',')
#             return round(float(parts[0].strip()), 1), round(float(parts[1].strip()), 1)
#     except Exception:
#         pass
#     return None, None


# def get_network_speed():
#     net1 = psutil.net_io_counters()
#     time.sleep(0.5)
#     net2 = psutil.net_io_counters()
#     sent_mbps = round((net2.bytes_sent - net1.bytes_sent) / 0.5 * 8 / 1_000_000, 2)
#     recv_mbps = round((net2.bytes_recv - net1.bytes_recv) / 0.5 * 8 / 1_000_000, 2)
#     return sent_mbps, recv_mbps


# def collect_stats():
#     cpu_percent  = psutil.cpu_percent(interval=0.5)
#     mem_percent  = psutil.virtual_memory().percent
#     disk         = psutil.disk_usage('C:/')
#     disk_percent = disk.percent
#     disk_used    = round(disk.used  / (1024 ** 3), 1)
#     disk_total   = round(disk.total / (1024 ** 3), 1)
#     disk_free    = round(disk.free  / (1024 ** 3), 1)

#     gpu_percent, gpu_temp = get_gpu_stats()
#     gpu_available = gpu_percent is not None

#     # Always use numbers — never None — so Jinja and JSON never choke
#     gpu_percent = gpu_percent if gpu_percent is not None else 0
#     gpu_temp    = gpu_temp    if gpu_temp    is not None else 0

#     net_sent, net_recv = get_network_speed()

#     alerts = []
#     if cpu_percent  > 80: alerts.append("High CPU utilization!")
#     if mem_percent  > 80: alerts.append("High Memory utilization!")
#     if disk_percent > 90: alerts.append("Low Disk Space!")
#     if gpu_available and gpu_percent > 90: alerts.append("High GPU utilization!")
#     if gpu_available and gpu_temp    > 85: alerts.append("High GPU Temperature!")

#     return {
#         "cpu_percent":   cpu_percent,
#         "mem_percent":   mem_percent,
#         "disk_percent":  disk_percent,
#         "disk_used":     disk_used,
#         "disk_total":    disk_total,
#         "disk_free":     disk_free,
#         "gpu_percent":   gpu_percent,
#         "gpu_temp":      gpu_temp,
#         "gpu_available": gpu_available,
#         "net_sent":      net_sent,
#         "net_recv":      net_recv,
#         "alerts":        alerts,
#     }


# @app.route("/")
# def index():
#     stats = collect_stats()
#     return render_template("index.html", **stats)


# @app.route("/stats")
# def stats_api():
#     return jsonify(collect_stats())


# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5001)

import time
import subprocess
import psutil

from flask import Flask, render_template, jsonify

app = Flask(__name__)


# -------------------------
# GPU USING NVIDIA-SMI
# -------------------------

def get_gpu_stats():

    try:

        result = subprocess.run(

            [
                'nvidia-smi',

                '--query-gpu=utilization.gpu,temperature.gpu',

                '--format=csv,noheader,nounits'
            ],

            capture_output=True,

            text=True,

            timeout=3

        )

        if result.returncode == 0:

            parts = result.stdout.strip().split(',')

            return (

                round(float(parts[0].strip()), 1),

                round(float(parts[1].strip()), 1)

            )

    except Exception:

        pass

    return None, None


# -------------------------
# NETWORK SPEED (FIXED)
# -------------------------

# prev_net = psutil.net_io_counters()

# prev_time = time.time()


def get_network_speed():
    net1 = psutil.net_io_counters()
    time.sleep(0.5)
    net2 = psutil.net_io_counters()
    sent_mbps = round((net2.bytes_sent - net1.bytes_sent) / 0.5 * 8 / 1_000_000, 2)
    recv_mbps = round((net2.bytes_recv - net1.bytes_recv) / 0.5 * 8 / 1_000_000, 2)
    return sent_mbps, recv_mbps


# -------------------------
# MAIN STATS FUNCTION
# -------------------------

def collect_stats():

    cpu_percent = psutil.cpu_percent(interval=None)

    mem_percent = psutil.virtual_memory().percent

    # Disk info

    disk_name = "C"

    disk = psutil.disk_usage('C:/')

    disk_percent = disk.percent

    disk_used = round(

        disk.used / (1024 ** 3),

        1

    )

    disk_total = round(

        disk.total / (1024 ** 3),

        1

    )

    disk_free = round(

        disk.free / (1024 ** 3),

        1

    )

    # GPU

    gpu_percent, gpu_temp = get_gpu_stats()

    gpu_available = gpu_percent is not None

    gpu_percent = gpu_percent if gpu_percent else 0

    gpu_temp = gpu_temp if gpu_temp else 0

    # Network

    net_sent, net_recv = get_network_speed()

    # Alerts

    alerts = []

    if cpu_percent > 80:
        alerts.append("High CPU utilization!")

    if mem_percent > 80:
        alerts.append("High Memory utilization!")

    if disk_percent > 90:
        alerts.append("Low Disk Space!")

    if gpu_available and gpu_percent > 90:
        alerts.append("High GPU utilization!")

    if gpu_available and gpu_temp > 85:
        alerts.append("High GPU Temperature!")

    return {

        "cpu_percent": cpu_percent,

        "mem_percent": mem_percent,

        "disk_percent": disk_percent,

        "disk_used": disk_used,

        "disk_total": disk_total,

        "disk_free": disk_free,

        "disk_name": disk_name,   # NEW

        "gpu_percent": gpu_percent,

        "gpu_temp": gpu_temp,

        "gpu_available": gpu_available,

        "net_sent": net_sent,

        "net_recv": net_recv,

        "alerts": alerts,

    }


# -------------------------
# ROUTES
# -------------------------

@app.route("/")
def index():

    stats = collect_stats()

    return render_template(

        "index.html",

        **stats

    )


@app.route("/stats")
def stats_api():

    return jsonify(

        collect_stats()

    )


# -------------------------
# RUN SERVER
# -------------------------

if __name__ == '__main__':

    app.run(

        debug=True,

        host='0.0.0.0',

        port=5001

    )