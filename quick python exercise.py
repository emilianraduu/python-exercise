import sys
import psutil  
import threading
import logging 
import os

def set_interval(func, sec): 
    def func_wrapper():
        set_interval(func, sec) 
        func()  
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def check_process(arg_process):
    isAlive = False
    for proc in psutil.process_iter():
        try:
            processName = proc.name()
            processID = proc.pid
            if processName == arg_process:
                proc.terminate()
                isAlive = True
                logging.info('your text goes here')
                logging.error('your text goes here')
                logging.debug('your text goes here')
            else:
                pass
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    if isAlive == False:
        print('closed')
def main():
    process_name = None
    time = None
    log_file = None
    
    if len(sys.argv) < 1:
        raise Exception('Not enough params')
    if sys.argv[1] is not None:
        process_name = sys.argv[1]

    else:
       raise Exception('Missing process name')

    if sys.argv[2] is not None:
        time = int(sys.argv[2])

    else:
       raise Exception('Missing time')

    if sys.argv[3] is not None:
        log_file = sys.argv[3]
    else:
       raise Exception('Missing log file')
    logging.basicConfig(filename=log_file, level=logging.INFO)
    lFunction = lambda : check_process(process_name)
    set_interval(lFunction, time)
   


if __name__ == "__main__":
    main()
