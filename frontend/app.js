// frontend/app.js
document.addEventListener('DOMContentLoaded', function() {
    fetch('http://192.168.1.100:5000/devices') // Remplacez l'adresse IP par celle de votre Raspberry Pi
        .then(response => response.json())
        .then(data => {
            const devicesDiv = document.getElementById('devices');
            data.forEach(device => {
                const deviceElement = document.createElement('div');
                deviceElement.textContent = `${device.name} - ${device.ip_address}`;
                devicesDiv.appendChild(deviceElement);
            });
        })
        .catch(error => console.error('Error fetching devices:', error));
});
//////////////////////// envoi //////////////////////

// frontend/app.js
document.getElementById('addDeviceForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const formData = new FormData(this);
    const deviceData = {
        name: formData.get('name'),
        ip_address: formData.get('ip_address')
    };

    fetch('http://192.168.1.100:5000/devices', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(deviceData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Device added successfully:', data);
        // Mettre à jour l'interface utilisateur ou effectuer d'autres actions si nécessaire
    })
    .catch(error => console.error('Error adding device:', error));
});
