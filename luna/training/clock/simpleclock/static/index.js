// use momentjs to display the time, nicely formatted.
// updates every second

function update() {
    time.innerHTML = moment().format('h:mm:ss a');
    }

update();
setInterval(update, 1000);
