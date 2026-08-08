import http.server
import socketserver
import os
import cgi

PORT = 8080

class UploadHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        html = '''
        <html>
        <body style="font-family: sans-serif; padding: 40px; text-align: center; background: #111; color: white;">
            <h2>Upload Your Profile Picture</h2>
            <p>Upload the photo you want to use for your portfolio.</p>
            <form enctype="multipart/form-data" method="POST" style="margin-top: 30px;">
                <input type="file" name="file" accept="image/*" style="font-size: 20px;"><br><br>
                <input type="submit" value="Upload to Portfolio" style="font-size: 20px; padding: 10px 20px; background: #00FF88; border: none; cursor: pointer; color: black; font-weight: bold; border-radius: 5px;">
            </form>
        </body>
        </html>
        '''
        self.wfile.write(html.encode())

    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type']}
        )
        
        if 'file' in form:
            fileitem = form['file']
            if fileitem.filename:
                # Always save as profile.jpg in the current directory
                filepath = os.path.join(os.getcwd(), 'profile.jpg')
                with open(filepath, 'wb') as f:
                    f.write(fileitem.file.read())
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><body style='font-family: sans-serif; text-align: center; padding: 40px; background: #111; color: white;'><h2>Success!</h2><p>Your profile picture is saved. You can close this tab and refresh your portfolio!</p></body></html>")
                return
                
        self.send_response(400)
        self.end_headers()
        self.wfile.write(b"Error: No file uploaded.")

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), UploadHandler) as httpd:
    print(f"Upload server running at http://localhost:{PORT}")
    httpd.serve_forever()
