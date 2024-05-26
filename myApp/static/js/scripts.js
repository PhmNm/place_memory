document.addEventListener("DOMContentLoaded", function() {
    const map = L.map('map').setView([10.806015, 106.643155], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
    }).addTo(map);

    let marker;

    map.on('click', function(e) {
        const { lat, lng } = e.latlng;
        if (marker) {
            marker.setLatLng(e.latlng);
        } else {
            marker = L.marker([lat, lng]).addTo(map);
        }
        document.getElementById('id_latitude').value = lat;
        document.getElementById('id_longitude').value = lng;
    });
});