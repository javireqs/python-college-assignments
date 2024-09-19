# Homework 13 - Web Service (Extra Features)
# This program uses http.server to serve the output of the program date -R on an available high port number. 
# Also, tells the user what the port number is so that they can access the service.
# CS 231 - Advanced Python


import http.server
import socketserver
import subprocess
import logging
import signal
import sys
import time
from collections import defaultdict

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Rate limiting settings
REQUEST_LIMIT = 5  # Maximum number of requests allowed per IP
TIME_WINDOW = 60   # Time window in seconds for rate limiting

# Dictionary to keep track of access records for each IP
access_records = defaultdict(list)

# Custom HTTP request handler
class DateHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        client_ip = self.client_address[0]  # Get the IP address of the client
        current_time = time.time()

        # Remove outdated access records
        access_records[client_ip] = [t for t in access_records[client_ip] if current_time - t < TIME_WINDOW]

        # Check if the client has exceeded the rate limit
        if len(access_records[client_ip]) >= REQUEST_LIMIT:
            logging.warning(f"Rate limit exceeded for {client_ip}")
            self.send_error(429, "Too Many Requests")
            return

        # Attempt to execute the 'date -R' command and send the output
        try:
            date_output = subprocess.check_output("date -R", shell=True).decode()
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(date_output.encode())
        except subprocess.SubprocessError as e:
            logging.error(f"Error executing date command: {e}")
            self.send_error(500)

# Function to find an available port
def find_available_port():
    with socketserver.TCPServer(("", 0), None) as s:
        return s.server_address[1]

# Find an available port and start the server
port = find_available_port()
httpd = socketserver.TCPServer(("", port), DateHandler)

# Signal handler for graceful shutdown
def signal_handler(signal, frame):
    logging.info('Shutting down server...')
    httpd.server_close()  # Close the server socket
    sys.exit(0)

# Register the signal handler for interrupt signal (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

# Log the server start and begin serving
logging.info(f"Server started on port {port}")
httpd.serve_forever()
