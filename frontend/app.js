
document.addEventListener('DOMContentLoaded', function() {
    fetchDevices();
    // Écouteur d'événement pour soumettre le formulaire d'ajout de périphérique
    document.getElementById('addDeviceForm').addEventListener('submit', function(event) {
        event.preventDefault();
        
        const formData = new FormData(this);
        const deviceData = {
            name: formData.get('name'),
            ip_address: formData.get('ip_address')
        };

        fetch('http:/10.19.4.7:5000/devices', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(deviceData)
        })
        .then(response => {
            if (response.ok) {
                console.log('Device added successfully.');
                // Actualiser la liste des périphériques après l'ajout
                fetchDevices();
            } else {
                console.error('Error adding device:', response.statusText);
            }
        })
        .catch(error => console.error('Error adding device:', error));
    });
});

function fetchDevices() {
    fetch('http://10.19.4.7:50000/devices')
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Error fetching devices:', response.statusText);
            }
        })
        .then(data => {
            const devicesDiv = document.getElementById('devices');
            devicesDiv.innerHTML = ''; // Effacer le contenu précédent

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
        .catch(error => console.error(error));
}
