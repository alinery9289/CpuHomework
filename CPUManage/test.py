import time
import sqlite3
import multiprocessing  

    
def second_consume():
    sql= sqlite3.connect('db.sqlite3')
    cx= sql.cursor()
    while 1:
        for i in range(3*100):
            this_sets =cx.execute("select * from CPUInfo_Setting where cpu_is_local='local'")
            cpu_state_set = int(this_sets.fetchone()[2])
            for j in range(1600*1000*(cpu_state_set-5)/100/5+1):
                pass
            time.sleep(0.01)

def test():
    t1= multiprocessing.Process(target = second_consume)
    t1.start()
    t2= multiprocessing.Process(target = second_consume)
    t2.start()
    t3= multiprocessing.Process(target = second_consume)
    t3.start()
    t4= multiprocessing.Process(target = second_consume)
    t4.start()
    
if __name__=='__main__':
    multiprocessing.freeze_support()
#     second_consume()
    test()

