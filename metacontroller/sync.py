from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Controller(BaseHTTPRequestHandler):
    def sync(self, parent, children):
        # Compute status based on observed state.
        desired_status = {
            "pods": len(children["Pod.v1"])
        }

        # Generate the desired child object(s).
        who = parent.get("spec", {}).get("who", "World")
        desired_pods = [
            {
                "apiVersion": "v1",
                "kind": "Pod",
                "metadata": {
                    "name": parent["metadata"]["name"]
                },
                "spec": {
                    "restartPolicy": "OnFailure",
                    "containers": [
                        {
                            "name": "hello",
                            "image": "busybox",
                            "command": ["echo", f"Hello, {who}!"]
                        }
                    ]
                }
            }
        ]

        return {"status": desired_status, "children": desired_pods}

    def do_post(self):
        # Serve the sync() function as a JSON webhook.
        observed = json.loads(self.rfile.read(int(self.headers.get("content-length"))))
        desired = self.sync(observed["parent"], observed["children"])

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(desired).encode())


HTTPServer(("", 80), Controller).serve_forever()
