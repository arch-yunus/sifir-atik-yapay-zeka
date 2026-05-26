import json
import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Sıfır Atık YZ Backend")

# CORS ayarları (Arayüzün API'ye erişebilmesi için)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Aktif websocket bağlantılarını tutacak liste
active_connections = []

class WasteData(BaseModel):
    type: str
    confidence: float
    timestamp: str

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            # Client'tan gelen ping vs mesajları dinle (opsiyonel)
            data = await websocket.receive_text()
    except WebSocketDisconnect:
        active_connections.remove(websocket)

@app.post("/api/detect")
async def detect_waste(data: WasteData):
    """
    Edge cihazından (Raspberry Pi/Jetson) gelen atık verisini alır
    ve Web Dashboard'a bağlı olan tüm WebSocket istemcilerine anında iletir.
    """
    # Veriyi JSON'a çevir
    message = json.dumps(data.dict())
    
    # Tüm bağlı dashboard client'larına yolla
    disconnected_clients = []
    for connection in active_connections:
        try:
            await connection.send_text(message)
        except Exception:
            disconnected_clients.append(connection)
            
    # Kopan bağlantıları temizle
    for client in disconnected_clients:
        if client in active_connections:
            active_connections.remove(client)
            
    return {"status": "success", "message": "Atık verisi arayüze iletildi."}

if __name__ == "__main__":
    import uvicorn
    # Test için lokalde başlatma komutu: uvicorn main:app --reload
    uvicorn.run(app, host="0.0.0.0", port=8000)
