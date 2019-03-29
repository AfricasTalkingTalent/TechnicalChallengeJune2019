// import npm modules
const bodyParser = require('body-parser');
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
const creds = {
  apiKey: 'ae18e1598bba0a0b54b13af0444e58653fdfaae0901d741b706e081091b912ab',
  username: 'sandbox'
};
const AfricasTalking = require('africastalking')(creds);

// configure body parser to accept json & form-data
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// tell the server what port to listen on
const port = process.env.PORT || 3000;
app.set('port', port);
app.listen(app.get('port'), () => {
  console.log('Listening on port ' + app.get('port'));
});

module.exports = router;