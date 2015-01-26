import requests,time,thread

def latency_test(threadName):
    start = time.time()*1000
    r = requests.get("http://192.168.1.142")
    try:
        print "%s: %d" % (threadName,time.time()*1000 - start)
    except:
        print "didn't work"

count = 0
while(count < 100):
    count+=1;
    try:
        thread.start_new_thread(latency_test,("Thread %d" % count,))
    except:
        print "Unable to start thread %d" % count

latency_test("lastone")
