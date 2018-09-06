function getElevation() {
  var map = new google.maps.Map(document.getElementById('output'), {
        zoom: 10,
        center: new google.maps.LatLng(42.3550071, -98.7512188),
        mapTypeId: google.maps.MapTypeId.TERRAIN
   });
  axios.post('http://127.0.0.1:5000/input', {
        slat: window.ALat.toFixed(7),
        slon: window.ALon.toFixed(7),
        dlat: window.BLat.toFixed(7),
        dlon: window.BLon.toFixed(7)
    })
    .then(function (response) {
        var marker, i;
        var pc = Array();
        path1 = response.data['0'];
        console.log(path1);
        for(i= 0; i < path1.length; i++) {
          pc.push({
                lat : path1[i][0],
                lng : path1[i][1]
          });
          marker = new google.maps.Marker({
            position: new google.maps.LatLng(path1[i][0], path1[i][1]),
            map: map
          });
        }
        var line = new google.maps.Polyline({
          path: pc,
//        path: [
//                new google.maps.LatLng(40.2980556,-96.2021599),
//                new google.maps.LatLng(40.3644088,-100.3611508)
//               ],
        geodesic : true,
        strokeColor: "#FF0000",
        strokeOpacity: 1.0,
        strokeWeight: 1,
        map: map

        });
        //console.log(response.data);
    })
    .catch(function (error) {
      console.log(error);
    });
}

function validate() {



}