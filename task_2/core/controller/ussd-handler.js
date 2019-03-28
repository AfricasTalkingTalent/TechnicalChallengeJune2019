const UssdMenu = require('ussd-menu-builder')
require('dotenv').config();
const smsHandler =require( './sms-handler')


const utils = require('../utils/utils')

exports.loadUSSDCallback = async (req, res, next) => {
    let menu = new UssdMenu();
    let sessions = {}

    try {
        let args = {
            phoneNumber: req.body.phoneNumber,
            sessionId: req.body.sessionId,
            serviceCode: req.body.serviceCode,
            text: req.body.text,
        };
        let sessionConfig = {
            start(sessionId, callback) {
                if (!(sessionId in sessions)) sessionId[sessionId] = {}
                callback()
            },
            end(sessionId, callback) {
                delete sessions[sessionId]
            },
            set(sessionId, key, value, callback) {
                sessions[sessionId][key] = value
                callback()
            },
            get(sessionId, key, callback) {
                let value = sessions[sessionId][key]
                callback(null, value)
            }
        }
        menu.sessionConfig(sessionConfig)

        menu.startState({
            run: () => {
                menu.con('User Registration' +
                    '\n1. Register' +
                    '\n2. Developed By: '
                );
            },
            next: {
                '1': 'registration',
                '2': 'developedBy'
            }
        });

        menu.state('registration', {
            run: function () {
                menu.con('Enter Username');
                let username = menu.val;


            },
            next: {
                '*[a-zA-Z]+': 'registration.username'

            }

        })
        menu.state('registration.username',{
            run: function () {
                menu.con('Enter Email Address')
            },
            next:{
                '*\\w+@\\w+\\.\\w+': 'emailAddress'
            }
        })

        menu.state('emailAddress', {
            run: function () {
                smsHandler.sendMessage(menu.args.phoneNumber)
                menu.end("sms verification sent")
            },

        })

        menu.state('developedBy', {
            run: async () => {
                menu.end("Kamau Brian")
            }
        })


        menu.run(args, resMsg => {
            res.send(resMsg);
        });

    } catch (e) {
        console.log(e.message);
        res.status(500).send({
            message: ' Error Occurred',
            error: e.message
        })
    }
}