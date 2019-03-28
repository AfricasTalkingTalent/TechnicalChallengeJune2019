const express = require('express');
const ussdController = require('../controller/ussd-handler');
const router = express.Router();

router.post('/ussd-callback',ussdController.loadUSSDCallback);


module.exports = router;
