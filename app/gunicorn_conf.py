import multiprocessing

bind = 'unix:/tmp/gunicorn_my_app.sock'
backlog = 2048

workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
worker_connections = 1000
max_requests = 0
timeout = 30
keepalive = 2
debug = True
spew = False

proc_name = 'gunicorn_my_app'
