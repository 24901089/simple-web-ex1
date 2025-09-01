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
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()