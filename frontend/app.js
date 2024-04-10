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
