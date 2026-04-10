#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple HTTP Server with proper SVG MIME type support
"""
import http.server
import socketserver
import mimetypes
import os

# 确保SVG文件类型被正确识别
mimetypes.add_type('image/svg+xml', '.svg')
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('text/css', '.css')

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # 添加CORS头，允许跨域访问
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()
    
    def guess_type(self, path):
        """重写guess_type方法以确保正确的MIME类型"""
        base, ext = os.path.splitext(path)
        if ext == '.svg':
            return 'image/svg+xml'
        return super().guess_type(path)

if __name__ == '__main__':
    import os
    
    Handler = MyHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Server running at:")
        print(f"  - http://localhost:{PORT}")
        print(f"  - http://127.0.0.1:{PORT}")
        print(f"\nPress Ctrl+C to stop the server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\nServer stopped.")
