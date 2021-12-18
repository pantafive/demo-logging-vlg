# Demonstration of Vector.dev+Loki+Grafana stack

1. Run `make up` to start docker environment.
2. Add Loki data source at http://127.0.0.1:3000/datasources/new. Set url to `http://loki:3100`, other parameters left as default.
3. Open [Explorer](http://127.0.0.1:3000/explore) and select Loki Data Source.
4. Run example query:

    ```
    {event="log"}
    | json
    | json_log_level=~"DEBUG|INFO|WARNING|ERROR|CRITICAL"
    | line_format "{{.json_log_level}} \t {{.json_request_id}} \t {{.json_message}}"
    ```

5. `make clean` removes all containers of the project.
