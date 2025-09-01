# EX01 Developing a Simple Webserver
## Date:

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<!doctype html>
<HTML>
    <HEAD>
        <BODY BGCOLOR="CYAN">
    <TABLE BORDER="1" ALIGN="CENTER" BGCOLOR="PINK " CELLPADDING="10">
    <CAPTION><H1>LIST OF PROTOCOLS</H1></CAPTION>
        <TR>

            <TH>

                S.NO.
            </TH>
            <TH>
                NAME OF THE LAYERS
            </TH>
            <TH>
                NAME OF THE PROTOCOLS
            </TH>
        </TR>
    <TR><TD>1</TD><TD>APPLICATION</TD><TD>HTTP,FTP</TD></TR>
    <TR><TD>2</TD><TD>TRANSPORT LAYER</TD><TD>TCP & UDP</TD></TR>
    <TR><TD>3</TD><TD>NETWORK LAYER</TD><TD>IPV4 & IPV6</TD></TR>
    <TR><TD>4</TD><TD>PHYSICAL LAYER</TD><TD>ETHERNET</TD></TR>
</TABLE>
    
        
    </BODY>
</HTML>

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPSerAZZZAXDver(server_address,MyServer)
httpd.serve_forever()
```

## OUTPUT:
![alt text](<Screenshot 2025-08-30 040211.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
