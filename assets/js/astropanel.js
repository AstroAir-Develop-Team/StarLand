$(document).ready(function () {
    const url = location.protocol + '//' + location.hostname + (location.port ? ':' + location.port : '');
    const socket = io.connect(url, { path: location.pathname + 'socket.io' });
    socket.on('emit', function () {
        client.emit('PING');
    });
    socket.on('celestialdata', function (data) {
        $("#polaris_next_transit").html(data.polaris_next_transit);
        $("#polaris_alt").html(data.polaris_alt);
        $("#moon_phase").html(data.moon_phase + " (" + data.moon_light + "%)");
        $("#moon_rise").html(data.moon_rise);
        $("#moon_transit").html(data.moon_transit);
        $("#moon_set").html(data.moon_set);
        $("#moon_az").html(data.moon_az);
        $("#moon_alt").html(data.moon_alt);
        $("#moon_ra").html(data.moon_ra);
        $("#moon_dec").html(data.moon_dec);
        $(".moon_new").html(data.moon_new);
        $("#moon_full").html(data.moon_full);
        $("#sun_at_start").html(data.sun_at_start);
        $("#sun_ct_start").html(data.sun_ct_start);
        $("#sun_rise").html(data.sun_rise);
        $("#sun_transit").html(data.sun_transit);
        $("#sun_set").html(data.sun_set);
        $("#sun_ct_end").html(data.sun_ct_end);
        $("#sun_at_end").html(data.sun_at_end);
        $("#sun_az").html(data.sun_az);
        $("#sun_alt").html(data.sun_alt);
        $("#sun_ra").html(data.sun_ra);
        $("#sun_dec").html(data.sun_dec);
        $("#sun_equinox").html(data.sun_equinox);
        $(".sun_solstice").html(data.sun_solstice);
        $("#mercury_rise").html(data.mercury_rise);
        $("#mercury_transit").html(data.mercury_transit);
        $("#mercury_set").html(data.mercury_set);
        $("#mercury_az").html(data.mercury_az);
        $("#mercury_alt").html(data.mercury_alt);
        $("#venus_rise").html(data.venus_rise);
        $("#venus_transit").html(data.venus_transit);
        $("#venus_set").html(data.venus_set);
        $("#venus_az").html(data.venus_az);
        $("#venus_alt").html(data.venus_alt);
        $("#mars_rise").html(data.mars_rise);
        $("#mars_transit").html(data.mars_transit);
        $("#mars_set").html(data.mars_set);
        $("#mars_az").html(data.mars_az);
        $("#mars_alt").html(data.mars_alt);
        $("#jupiter_rise").html(data.jupiter_rise);
        $("#jupiter_transit").html(data.jupiter_transit);
        $("#jupiter_set").html(data.jupiter_set);
        $("#jupiter_az").html(data.jupiter_az);
        $("#jupiter_alt").html(data.jupiter_alt);
        $("#saturn_rise").html(data.saturn_rise);
        $("#saturn_transit").html(data.saturn_transit);
        $("#saturn_set").html(data.saturn_set);
        $("#saturn_az").html(data.saturn_az);
        $("#saturn_alt").html(data.saturn_alt);
        $("#uranus_rise").html(data.uranus_rise);
        $("#uranus_transit").html(data.uranus_transit);
        $("#uranus_set").html(data.uranus_set);
        $("#uranus_az").html(data.uranus_az);
        $("#uranus_alt").html(data.uranus_alt);
        $("#neptune_rise").html(data.neptune_rise);
        $("#neptune_transit").html(data.neptune_transit);
        $("#neptune_set").html(data.neptune_set);
        $("#neptune_az").html(data.neptune_az);
        $("#neptune_alt").html(data.neptune_alt);

        const pha = data.polaris_hour_angle;
        let pha_angle = 360 + pha * -1;
        pha_angle -= 180;
        const rotation = "rotate(" + pha_angle + "deg)";
        $("#polaris_marker").css("-ms-transform", rotation);
        $("#polaris_marker").css("-webkit-transform", rotation);
        $("#polaris_marker").css("transform", rotation);

        const phaH = String(parseInt(pha / 15));
        const phaMtmp = (pha / 15 - phaH) * 60;
        const phaM = String(parseInt(phaMtmp));
        const phaS = String(parseInt((phaMtmp - phaM) * 60));
        $("#pha").html(phaH.padStart(2, '0') + ":" + phaM.padStart(2, '0') + ":" + phaS.padStart(2, '0'));

        const pnt = data.polaris_next_transit.split(':');
        const p9h = (parseInt(pnt[0]) - 6);
        const p12h = (parseInt(pnt[0]) - 12);
        const p3h = (parseInt(pnt[0]) - 18);
        $("#polaris_next_3").html(p3h + ':' + pnt[1] + ':' + pnt[2]);
        $("#polaris_next_12").html(p12h + ':' + pnt[1] + ':' + pnt[2]);
        $("#polaris_next_9").html(p9h + ':' + pnt[1] + ':' + pnt[2]);

        if (parseFloat(data.mercury_alt) > 25) {
            $("#mercury").css("color", "#99cc00");
        } else if (parseFloat(data.mercury_alt) > 0) {
            $("#mercury").css("color", "#ff9900");
        } else {
            $("#mercury").css("color", "#fff");
        }

        if (parseFloat(data.venus_alt) > 25) {
            $("#venus").css("color", "#99cc00");
        } else if (parseFloat(data.venus_alt) > 0) {
            $("#venus").css("color", "#ff9900");
        } else {
            $("#venus").css("color", "#fff");
        }

        if (parseFloat(data.mars_alt) > 25) {
            $("#mars").css("color", "#99cc00");
        } else if (parseFloat(data.mars_alt) > 0) {
            $("#mars").css("color", "#ff9900");
        } else {
            $("#mars").css("color", "#fff");
        }

        if (parseFloat(data.jupiter_alt) > 25) {
            $("#jupiter").css("color", "#99cc00");
        } else if (parseFloat(data.jupiter_alt) > 0) {
            $("#jupiter").css("color", "#ff9900");
        } else {
            $("#jupiter").css("color", "#fff");
        }

        if (parseFloat(data.saturn_alt) > 25) {
            $("#saturn").css("color", "#99cc00");
        } else if (parseFloat(data.saturn_alt) > 0) {
            $("#saturn").css("color", "#ff9900");
        } else {
            $("#saturn").css("color", "#fff");
        }

        if (parseFloat(data.uranus_alt) > 25) {
            $("#uranus").css("color", "#99cc00");
        } else if (parseFloat(data.uranus_alt) > 0) {
            $("#uranus").css("color", "#ff9900");
        } else {
            $("#uranus").css("color", "#fff");
        }

        if (parseFloat(data.neptune_alt) > 25) {
            $("#neptune").css("color", "#99cc00");
        } else if (parseFloat(data.neptune_alt) > 0) {
            $("#neptune").css("color", "#ff9900");
        } else {
            $("#neptune").css("color", "#fff");
        }

        const ss = new Date(data.sun_solstice);
        const se = new Date(data.sun_equinox);
        if (ss < se) {
            $("#sun_solstice_first").css("display", "");
            $("#sun_solstice_second").css("display", "none");
        } else {
            $("#sun_solstice_first").css("display", "none");
            $("#sun_solstice_second").css("display", "");
        };

        const nm = new Date(data.moon_new);
        const fm = new Date(data.moon_full);
        if (nm < fm) {
            $("#new_moon_first").css("display", "");
            $("#new_moon_second").css("display", "none");
        } else {
            $("#new_moon_first").css("display", "none");
            $("#new_moon_second").css("display", "");
        };
    });
});

function togglepolaris() {
    document.getElementById("polaris").style.display = "block";
    document.getElementById("moon").style.display = "none";
    document.getElementById("sun").style.display = "none";
    document.getElementById("planets").style.display = "none";
}
function togglemoon() {
    document.getElementById("polaris").style.display = "none";
    document.getElementById("moon").style.display = "block";
    document.getElementById("sun").style.display = "none";
    document.getElementById("planets").style.display = "none";
}
function togglesun() {
    document.getElementById("polaris").style.display = "none";
    document.getElementById("moon").style.display = "none";
    document.getElementById("sun").style.display = "block";
    document.getElementById("planets").style.display = "none";
}
function toggleplanets() {
    document.getElementById("polaris").style.display = "none";
    document.getElementById("moon").style.display = "none";
    document.getElementById("sun").style.display = "none";
    document.getElementById("planets").style.display = "block";
}