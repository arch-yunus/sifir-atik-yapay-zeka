const wasteTypesConfig = {
    'PET': { name: 'PET Şişe', class: 'pet', icon: '🍾' },
    'HDPE': { name: 'HDPE Kutu', class: 'hdpe', icon: '🧴' },
    'Metal': { name: 'Alüminyum Kutu', class: 'metal', icon: '🥫' },
    'Reject': { name: 'Tanımlanamayan', class: 'reject', icon: '🗑️' }
};

const feedList = document.getElementById('feed-list');
let stats = {
    pet: 1245,
    hdpe: 856,
    metal: 342,
    reject: 89
};

function addLiveFeedItem(data) {
    const wasteConfig = wasteTypesConfig[data.type] || wasteTypesConfig['Reject'];
    
    // İstatistikleri güncelle
    if(data.type === 'PET') stats.pet++;
    else if(data.type === 'HDPE') stats.hdpe++;
    else if(data.type === 'Metal') stats.metal++;
    else stats.reject++;
    
    document.getElementById('pet-count').innerText = stats.pet.toLocaleString('en-US');
    document.getElementById('hdpe-count').innerText = stats.hdpe.toLocaleString('en-US');
    document.getElementById('metal-count').innerText = stats.metal.toLocaleString('en-US');
    document.getElementById('reject-count').innerText = stats.reject.toLocaleString('en-US');

    // DOM Elementi oluştur
    const item = document.createElement('div');
    item.className = 'feed-item';
    
    item.innerHTML = `
        <div class="feed-item-left">
            <span style="font-size: 1.5rem">${wasteConfig.icon}</span>
            <div>
                <span class="badge ${wasteConfig.class}">${wasteConfig.name}</span>
                <div class="time">${data.timestamp}</div>
            </div>
        </div>
        <div class="confidence">%${data.confidence.toFixed(1)}</div>
    `;

    // Listeye ekle (başa)
    feedList.insertBefore(item, feedList.firstChild);

    // Listeyi max 5 elemanda tut
    if (feedList.children.length > 5) {
        feedList.removeChild(feedList.lastChild);
    }
}

// WebSocket Bağlantısı Kurulumu
function connectWebSocket() {
    const ws = new WebSocket('ws://localhost:8000/ws');
    
    ws.onopen = () => {
        console.log("WebSocket bağlantısı başarılı. Edge verileri bekleniyor...");
        document.querySelector('.status-online').innerText = "Bağlı (Canlı)";
        document.querySelector('.status-online').style.background = "rgba(16, 185, 129, 0.2)";
    };
    
    ws.onmessage = (event) => {
        try {
            const data = JSON.parse(event.data);
            addLiveFeedItem(data);
        } catch (e) {
            console.error("Veri parse hatası:", e);
        }
    };
    
    ws.onclose = () => {
        console.log("WebSocket bağlantısı koptu. Yeniden bağlanılıyor...");
        document.querySelector('.status-online').innerText = "Bağlantı Koptu";
        document.querySelector('.status-online').style.background = "rgba(239, 68, 68, 0.2)";
        setTimeout(connectWebSocket, 3000);
    };
    
    ws.onerror = (err) => {
        console.error("WebSocket Hatası: ", err);
        ws.close();
    };
}

// Uygulama Başlangıcı
connectWebSocket();

// Saati Güncelle
setInterval(() => {
    document.getElementById('last-update').innerText = new Date().toLocaleTimeString('tr-TR');
}, 1000);
