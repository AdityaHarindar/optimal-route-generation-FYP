var geocoder = new google.maps.Geocoder();

function updateMarkerStatus(str) {
  //document.getElementById('markerStatus').innerHTML = str;
}

function updateMarkerPositionA(latLng) {
  document.getElementById('infoa').innerHTML = [
    latLng.lat(),
    latLng.lng()
  ].join(', ');
  window.ALat = latLng.lat();
  window.ALon = latLng.lng();
}

function updateMarkerPositionB(latLng) {
  document.getElementById('infob').innerHTML = [
    latLng.lat(),
    latLng.lng()
  ].join(', ');
  window.BLat = latLng.lat();
  window.BLon = latLng.lng();
}

function initialize() {
  var latLng = new google.maps.LatLng(42.3550071, -98.7512188);
  var latLng2 = new google.maps.LatLng(42.4213604, -100.2269898);
  var out1 = new google.maps.LatLng(40.29805556,-101.30027778);
  var out2 = new google.maps.LatLng(40.29805556,-94.72638889);
  var out3 = new google.maps.LatLng(42.88583333,-101.30027778);
  var out4 = new google.maps.LatLng(42.88583333,-94.72638889);
  var map = new google.maps.Map(document.getElementById('mapCanvas'), {
    zoom: 8,
    center: latLng,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  });

  var markerA = new google.maps.Marker({
    position: latLng,
    title: 'SOURCE',
    map: map,
    draggable: true
  });

  var markerB = new google.maps.Marker({
    position: latLng2,
    title: 'DESTINATION',
    map: map,
    draggable: true
  });

  var marker1 = new google.maps.Marker({
    position: out1,
    title: 'MAP 1',
    map: map,
    icon: 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
    draggable: false
  });
  var marker2 = new google.maps.Marker({
    position: out2,
    title: 'MAP 2',
    map: map,
    icon: 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
    draggable: false
  });
  var marker3 = new google.maps.Marker({
    position: out3,
    title: 'MAP 3',
    map: map,
    icon: 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
    draggable: false
  });
  var marker4 = new google.maps.Marker({
    position: out4,
    title: 'MAP 4',
    map: map,
    icon: 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
    draggable: false
  });

  // Update current position info.
  updateMarkerPositionA(latLng);
  updateMarkerPositionB(latLng2);

  google.maps.event.addListener(markerA, 'drag', function() {
    //updateMarkerStatus('Dragging...');
    updateMarkerPositionA(markerA.getPosition());
  });

  google.maps.event.addListener(markerA, 'dragend', function() {
    //updateMarkerStatus('Drag ended');
    geocodePosition(markerA.getPosition());
  });

  google.maps.event.addListener(markerB, 'drag', function() {
    //updateMarkerStatus('Dragging...');
    updateMarkerPositionB(markerB.getPosition());
  });

  google.maps.event.addListener(markerB, 'dragend', function() {
    //updateMarkerStatus('Drag ended');
    geocodePosition(markerB.getPosition());
  });

}

// Onload handler to fire off the app.
google.maps.event.addDomListener(window, 'load', initialize);