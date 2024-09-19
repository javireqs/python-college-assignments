# Homework 12 - Data Encodings
# This program uses http.server to serve the output of the program date -R on an available high port number. 
# Also, tells the user what the port number is so that they can access the service.
# CS 231 - Advanced Python

import http.server
import socketserver
import subprocess
from threading import Thread

# Define a handler to serve the output of the `date -R` command
class DateHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        # Run the `date -R` command and get the output
        date_output = subprocess.check_output("date -R", shell=True).decode()
        # Write the output to the response
        self.wfile.write(date_output.encode())

# Find an available high port number
def find_available_port():
    with socketserver.TCPServer(("", 0), None) as s:
        return s.server_address[1]

port = find_available_port()

# Start the server in a separate thread so it doesn't block the main thread
def start_server():
    with socketserver.TCPServer(("", port), DateHandler) as httpd:
        httpd.serve_forever()

# Start the server in a new thread
thread = Thread(target=start_server)
thread.start()

# Print the port number so the user knows where to connect
print(f"Server started on port {port}")
