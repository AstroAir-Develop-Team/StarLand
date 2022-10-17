function LoadMap() {
    document.getElementById("map").firstChild.data = "";

    /* Set default to Warsaw, Poland */
    let lon = 21.017532;
    let lat = 52.237049;

    let map = new ol.Map({
        target: "map",
        layers: [
            new ol.layer.Tile({
                source: new ol.source.OSM()
            })
        ],
        view: new ol.View({
            center: ol.proj.fromLonLat([lon, lat]),
            zoom: 4
        })
    });

    let center = new ol.geom.Point(
        ol.proj.transform([lon, lat], 'EPSG:4326', 'EPSG:3857')
    );

    let iconFeature = new ol.Feature({
        geometry: center
    });

    let iconStyle = new ol.style.Style({
        image: new ol.style.Icon({
            anchor: [0.5, 1.0],
            anchorXUnits: 'fraction',
            anchorYUnits: 'fraction',
            src: 'assets/img/marker.png'
        })
    });

    iconFeature.setStyle(iconStyle);

    let vectorSource = new ol.source.Vector({
        features: [iconFeature]
    });

    let vectorLayer = new ol.layer.Vector({
        source: vectorSource
    });

    map.addLayer(vectorLayer);
}

function UpdateMapPos(lon, lat) {
    iconFeature.setGeometry(new ol.geom.Point(ol.proj.transform([lon, lat], 'EPSG:4326', 'EPSG:3857')));
    map.getView().animate({
        center: ol.proj.fromLonLat([lon, lat]),
        duration: 1000
    });
}

$(document).ready(function () {
    const url = location.protocol + '//' + location.hostname + (location.port ? ':' + location.port : '');
    const socket = io.connect(url, { path: location.pathname + '/socket.io' });
    socket.on('gpsdata', function (gps) {
        $("#gpstime").html(gps.gpstime);
        $("#latitude").html(gps.latitude);
        $("#longitude").html(gps.longitude);
        $("#altitude").html(gps.altitude);
        $("#mode").html(gps.mode);
        $("#hdop").html(gps.hdop);
        $("#vdop").html(gps.vdop);

        if (gps.gpstime) {
            let d = new Date(gps.gpstime);
            let date = d.getUTCFullYear() + "-" + ("0" + (d.getUTCMonth() + 1)).substr(-2) + "-" + ("0" + d.getUTCDate()).substr(-2) + "T" + ("0" + d.getUTCHours()).substr(-2) + ":" + ("0" + d.getUTCMinutes()).substr(-2) + ":" + ("0" + d.getUTCSeconds()).substr(-2);
            $("#gtime").html(date);
        }

        if (gps.latitude && gps.longitude) {
            let lat = gps.latitude;
            let lon = gps.longitude;
            let lat_sign, lon_sign;

            UpdateMapPos(lon, lat);

            if (lat < 0) {
                lat_sign = '-';
            } else {
                lat_sign = '';
            }

            if (lon < 0) {
                lon_sign = '-';
            } else {
                lon_sign = '';
            }

            lat = Math.abs(lat);
            lon = Math.abs(lon);

            let latdeg = parseInt(lat);
            let latmin = parseInt((lat - latdeg) * 3600 / 60);
            let latsec = ((lat - latdeg - latmin / 60) * 3600).toFixed(4);
            let londeg = parseInt(lon);
            let lonmin = parseInt((lon - londeg) * 3600 / 60);
            let lonsec = ((lon - londeg - lonmin / 60) * 3600).toFixed(4);
            let latrad = lat_sign + latdeg + ":" + ("0" + latmin).substr(-2) + ":" + ("0" + latsec).substr(-7);
            let lonrad = lon_sign + londeg + ":" + ("0" + lonmin).substr(-2) + ":" + ("0" + lonsec).substr(-7);
            $("#lat").html(latrad);
            $("#lon").html(lonrad);
        }

        if (gps.sschart) {
            $("#sschart").attr("src", "data:image/png;base64," + gps.sschart);
        }

        if (gps.skymap) {
            $("#skymap").attr("src", "data:image/png;base64," + gps.skymap);
        }

        if (gps.satellites) {
            let satellites = "<table><tr><th colspan=5 align=left><h2>Visible Satellites<h2></th></tr><tr><th>PRN</th><th>Elevation</th><th>Azimuth</th><th>SS</th><th>Used</th></tr>";
            let used;
            for (const sat in gps.satellites) {
                if (gps.satellites[sat]['used']) {
                    used = 'Y';
                } else {
                    used = 'N';
                }
                satellites = satellites + "<tr align=right><td>" + gps.satellites[sat]['PRN'] + "</td><td>" + gps.satellites[sat]['el'] + "</td><td>" + gps.satellites[sat]['az'] + "</td><td>" + gps.satellites[sat]['ss'] + "</td><td>" + used + "</td></tr>";
            }
            satellites = satellites + "</table>";

            $("#sats").html(gps.satellites.length);
            $("#gpssats").html(satellites);
        }

        if (typeof (gps.mode) == 'number') {
            if (gps.mode == 3) {
                $("#gpsfix").html('3D');
                $("#gpsfix").removeClass("blink");
                $("#gpsfix_obtained").addClass("gpsfix_obtained");
            } else if (gps.mode == 2) {
                $("#gpsfix").html('2D');
                $("#gpsfix").removeClass("blink");
                $("#gpsfix_obtained").addClass("gpsfix_obtained");
            } else {
                $("#gpsfix").html('waiting...');
                $("#gpsfix").addClass("blink");
                $("#gpsfix_obtained").removeClass("gpsfix_obtained");
            }
        }
    });
});