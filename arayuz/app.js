// Simüle edilmiş atık verileri
const wasteTypes = [
    { type: 'PET', name: 'PET Şişe', class: 'pet', icon: '🍾' },
    { type: 'HDPE', name: 'HDPE Kutu', class: 'hdpe', icon: '🧴' },
    { type: 'Metal', name: 'Alüminyum Kutu', class: 'metal', icon: '🥫' }
];

const feedList = document.getElementById('feed-list');
let stats = {
    pet: 1245,
    hdpe: 856,
    metal: 342,
    reject: 89
};

// Sayıları güncelleme animasyonu
function animateValue(obj, start, end, duration) {
    let startTimestamp = null;
    const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        obj.innerHTML = Math.floor(progress * (end - start) + start).toLocaleString('en-US');
        if (progress < 1) {
            window.requestAnimationFrame(step);
        }
    };
    window.requestAnimationFrame(step);
}

// Yeni atık tespiti simülasyonu
function addLiveFeedItem() {
    const randomWaste = wasteTypes[Math.floor(Math.random() * wasteTypes.length)];
    const confidence = (Math.random() * (99.9 - 85.0) + 85.0).toFixed(1);
    
    // İstatistikleri güncelle
    if(randomWaste.type === 'PET') stats.pet++;
    if(randomWaste.type === 'HDPE') stats.hdpe++;
    if(randomWaste.type === 'Metal') stats.metal++;
    
    document.getElementById('pet-count').innerText = stats.pet.toLocaleString('en-US');
    document.getElementById('hdpe-count').innerText = stats.hdpe.toLocaleString('en-US');
    document.getElementById('metal-count').innerText = stats.metal.toLocaleString('en-US');

    // DOM Elementi oluştur
    const item = document.createElement('div');
    item.className = 'feed-item';
    
    const now = new Date();
    const timeStr = now.toLocaleTimeString('tr-TR');

    item.innerHTML = `
        <div class="feed-item-left">
            <span style="font-size: 1.5rem">${randomWaste.icon}</span>
            <div>
                <span class="badge ${randomWaste.class}">${randomWaste.name}</span>
                <div class="time">${timeStr}</div>
            </div>
        </div>
        <div class="confidence">%${confidence}</div>
    `;

    // Listeye ekle (başa)
    feedList.insertBefore(item, feedList.firstChild);

    // Listeyi max 5 elemanda tut
    if (feedList.children.length > 5) {
        feedList.removeChild(feedList.lastChild);
    }
}

// Başlangıçta 3 sahte veri ekle
for(let i=0; i<3; i++) {
    addLiveFeedItem();
}

// Her 4 saniyede bir yeni atık tespiti simüle et
setInterval(addLiveFeedItem, 4000);

// Saati Güncelle
setInterval(() => {
    document.getElementById('last-update').innerText = new Date().toLocaleTimeString('tr-TR');
}, 1000);
