let map;
document.addEventListener("DOMContentLoaded", function() {
    map = L.map('map').setView([10.806015, 106.643155], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
    }).addTo(map);

    let marker;

    let form_title = document.getElementById('form-title');

    if (form_title) {
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
    } else {
        fetch('/api/load-memory/')
            .then(response => response.json())
            .then(data => {
                data.forEach(item => {
                    L.marker([item.latitude, item.longitude])
                        .addTo(map)
                        .bindPopup(`<h4> ${item.place_name} </h4> <p> ${item.comments} </p>`);
                
                map.setView([data[0].latitude, data[0].longitude], 13);
                });
            });
    }
});

function navigateToMarker(lat, long) {
    map.setView([lat, long], 13);
}