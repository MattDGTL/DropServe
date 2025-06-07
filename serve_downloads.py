import http.server
import os
import sys

# This handler makes every file download when clicked in the browser.
class DownloadHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Only force download for files, not for the directory listing
        if self.path != "/" and not self.path.endswith("/"):
            self.send_header(
                'Content-Disposition',
                f'attachment; filename="{self.path.split("/")[-1]}"'
            )
        super().end_headers()

if __name__ == "__main__":
    # Serve files from the /webfiles directory (set by the Docker mount)
    os.chdir("/webfiles")
    # Use the first argument as the port, default to 8000 if not provided
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    http.server.test(HandlerClass=DownloadHandler, port=port)
