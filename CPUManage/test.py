import time
import sqlite3
import multiprocessing


def second_consume():
    sql= sqlite3.connect('db.sqlite3')
    cx= sql.cursor()
    while 1:
        for i in range(2*100):
            this_sets =cx.execute("select * from CPUInfo_Setting where cpu_is_local='local'")
            cpu_state_set = int(this_sets.fetchone()[2])
            for j in range(2500*1000*(cpu_state_set)/100/7 +1):
                pass
            time.sleep(0.01)

def test():
    t={}
    for i in range(16):
        t[i]= multiprocessing.Process(target = second_consume)
        t[i].start()


if __name__=='__main__':
    multiprocessing.freeze_support()
#     second_consume()
    test()
