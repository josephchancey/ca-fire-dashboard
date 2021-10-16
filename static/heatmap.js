// set the map center
var heatmap = L.map("heatmap", {
    center: [38.573, -121,494],
    zoom: 5
});

// add the tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(heatmap);


// load fire data
d3.json(`/inactive/fires`).then(function(fires){
    
    console.log(fires);

    var heatArray = [];

    for (var i = 0; i < fires.length; i++) {
        var location = [fires[i].Latitude, fires[i].Latitude];

        if (location) {
            heatArray.push(location);
        }
    }

    var heat = L.heatLayer(heatArray, {
        radius: 25,
        blur: 35
    }).addTo(heatmap);

})
