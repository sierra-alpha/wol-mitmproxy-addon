# wol-mitmproxy-addon
An addon for the tool mitmproxy which filters requests for specific servers, pauses the request, checks if the server is awake, wakes it if needed then lets the request continue.
mitmdump --listen-host 192.168.0.60 --ssl-insecure --mode reverse:tls://obsidian.sierraalpha.co.nz:9090 --mode reverse:dtls://obsidian.sierraalpha.co.nz:9090 -s wol_mitmproxy_addon/main.py --listen-port 9090
