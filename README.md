# Safe Slowloris Demonstration Script

This repository contains a **controlled, educational demonstration** of the Slowloris technique using Python.

>  **Ethical & Legal Notice**  
> This script is intended **only** for:
> - Local testing environments (e.g., `localhost`)
> - Personal labs and educational / research purposes  
> **Do not** use this against any system you do not own or do not have **explicit written permission** to test.

---

##  What Is This Script?

The script shows how sending **incomplete HTTP requests** can keep many connections open to a server at once.  
By slowly sending headers and small keep-alive lines, it prevents the server from closing the connections, which can help you understand how resource-exhaustion attacks like **Slowloris** work in practice.

This is a **learning tool** to:

- Observe TCP connections in tools like Wireshark
- Understand how HTTP requests are structured
- See how slow, partial requests behave on a web server

---

##  Technical Overview

The script uses the following Python standard libraries:

- `argparse` – parse command-line arguments
- `socket` – create raw TCP connections
- `time` – add delays between transmissions
- `threading` – manage multiple concurrent connections

### `slow_connection` Function

For each connection, this function:

1. Opens a **TCP connection** to the target host and port.
2. Sends a **partial `GET` HTTP request**.
3. Sends HTTP **headers one by one**, with a configurable delay between each header.
4. Continues to send **small keep-alive lines** so the server keeps the connection open.
5. If the server closes the connection or an error occurs, it prints a termination message.

### `main` Function

The main function is responsible for:

- Parsing command-line arguments.
- Starting multiple threads, each running `slow_connection`.
- Keeping all threads alive using `join()` so the process does not exit early.

---

##  Command-Line Arguments

The script accepts the following arguments:

- `-t`, `--target`  
  **Required.** Hostname or IP address of the server (e.g. `localhost`).

- `-p`, `--port`  
  Server port to connect to.  
  **Default:** `8080`

- `-c`, `--connections`  
  Number of concurrent TCP connections to open.  
  **Default:** `5`

- `-i`, `--interval`  
  Delay (in seconds) between sending headers / keep-alive lines.  
  **Default:** `10`

---

##  Example Usage (Localhost Only)

```bash
python ethical_DD0S.py -t localhost -p 8080 -c 3 -i 5
