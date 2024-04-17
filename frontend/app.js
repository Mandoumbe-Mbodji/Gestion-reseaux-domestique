document.addEventListener('DOMContentLoaded', function() {
    fetch('http://127.0.0.1:5000/devices')
        .then(response => response.json())
        .then(data => {
            const devicesDiv = document.getElementById('devices');
            data.forEach(device => {
                // Créer un conteneur pour chaque appareil
                const deviceContainer = document.createElement('div');
                deviceContainer.classList.add('device');

                // Créer un élément pour le nom de l'appareil
                const nameElement = document.createElement('h2');
                nameElement.textContent = device.name;

                // Créer un élément pour l'adresse IP de l'appareil
                const ipElement = document.createElement('p');
                ipElement.textContent = `IP: ${device.ip_address}`;

                // Ajouter les éléments au conteneur de l'appareil
                deviceContainer.appendChild(nameElement);
                deviceContainer.appendChild(ipElement);

                // Ajouter le conteneur de l'appareil à la liste des appareils
                devicesDiv.appendChild(deviceContainer);
            });
        })
        .catch(error => console.error('Error fetching devices:', error));
});

document.getElementById('addDeviceForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const formData = new FormData(this);
    const deviceData = {
        name: formData.get('name'),
        ip_address: formData.get('ip_address')
    };

    fetch('http://127.0.0.1:5000/devices', {
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
