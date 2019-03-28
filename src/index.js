// import npm modules
const express = require('express');
const jade = require('jade');
const path = require('path');

// const routes = require('./routes/index');
const router = express.Router();

const os = require('os');
const ifaces = os.networkInterfaces();

const ips = [];

Object.keys(ifaces).forEach(function (ifname) {
    var alias = 0;
    ifaces[ifname].forEach(function (iface) {
        if ('IPv4' !== iface.family || iface.internal !== false) {
            // skip over internal (i.e. 127.0.0.1) and non-ipv4 addresses
            return;
        }
        ips.push(iface.address);
    });
});

// routes
const ussdRoutes = require('./routes/ussd');

const app = express();

// view engine setup
app.set('views', path.join(__dirname, '../views'));
app.set('view engine', 'jade');

// Africa's Talking API configuration
APIConfig = require('./config');
// const AfricasTalking = require('africastalking')(APIConfig);

// tell the server what port to listen on
const port = process.env.PORT || 3000;
app.set('port', port);
app.listen(app.get('port'), () => {
  console.log('Listening on port ' + app.get('port'));
});

module.exports = router;