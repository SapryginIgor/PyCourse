from multiprocessing import Queue, Pipe, Process
import queue
import time
import codecs
import sys

start = time.time()

def A(main_pipe, abq):
    while True:
        s = main_pipe.recv()
        s = s.lower()
        abq.put(s)
        time.sleep(5)

def B(abq, mainq):
    while True:
        s = abq.get()
        rot = codecs.encode(s, 'rot_13')
        print("ENCODED MESSAGE: {}, TIME: {}".format(rot, time.time()-start),flush=True)
        mainq.put(rot)

if __name__ == '__main__':
    a_conn, main_conn = Pipe()
    abq = Queue()
    mainq = Queue()
    pa = Process(target=A, args=(a_conn,abq))
    pb = Process(target=B, args=(abq, mainq))
    pa.start()
    pb.start()
    while True:
            s = sys.stdin.readline()
            if s == '':
                print("Ending main process...")
                pa.terminate()
                pb.terminate()
                break
            main_conn.send(s)
            try:
                while True:
                    msg = mainq.get_nowait()
                    # print("DECODED MESSAGE: {}, TIME: {}".format(codecs.decode(msg, 'rot_13'), time.time()-start))
            except queue.Empty:
                pass
            
    
