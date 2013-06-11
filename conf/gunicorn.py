import multiprocessing

bind = '127.0.0.1:8888'
logfile = "/tmp/blog.log"
workers = multiprocessing.cpu_count() * 2 + 1
debug = False
