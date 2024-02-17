from waitress import serve
from app import app


serve(
    app, 
    host='192.168.2.223', 
    port=80,
    threads=6
)