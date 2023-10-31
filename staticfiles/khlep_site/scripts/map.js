var map = L.map("mapid").setView(
   [57.154, -2.08], 6
)

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data & copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    minZoom: 4,
    id: 'raincor/cktyvcl2e1bns17sc9f3cfgyq',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoicmFpbmNvciIsImEiOiJja3R1bTVzZ2kyMWg4MnZwbm9hZXZzdmVrIn0.3JM64Knf4fHYlL2gAB-_pQ'

}).addTo(map);

