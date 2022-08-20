var APIKEY="cqxFtmRGtpFHewpbRAhaFFfdv0vfi1sQ";

const Tamil_nadu = {lng: 80.270721, lat: 13.082680};
 
var map = tt.map({
  key: APIKEY,
  container: 'map',
  center: Tamil_nadu,
  zoom: 6,
});

var markers=[]

map.on('click',function(event){
    console.log(event)
    var marker = new tt.Marker().setLngLat(event.lngLat).addTo(map)
    markers.push(marker)
})

var displayRoute = function(geoJSON){
    routeLayer = map.addLayer
    ({
        'id':'route',
        'type':'line',
        'source':{
            'data': geoJSON

        },
        'paint':{
            'line-color' : 'red',
            'line-width': 5
        }
    });
}

var createRoute = function(){
    var routeOptions={
        key: 'cqxFtmRGtpFHewpbRAhaFFfdv0vfi1sQ',
        locations: [],
      
    }
    for (marker of markers){
        routeOptions.locations.push(marker.getLngLat())
    
    }

    tt.services.calculateRoute(routeOptions)
      .then(function(response) {
          var geojson = response.toGeoJson();
          map.addLayer({
              'id': 'route',
              'type': 'line',
              'source': {
                  'type': 'geojson',
                  'data': geojson
              },
              'paint': {
                  'line-color': 'red',
                  'line-width': 5
              }
          });
          var bounds = new tt.LngLatBounds();
          geojson.features[0].geometry.coordinates.forEach(function(point) {
              bounds.extend(tt.LngLat.convert(point));
          });
          map.fitBounds(bounds, {padding: 20});
      });
}
