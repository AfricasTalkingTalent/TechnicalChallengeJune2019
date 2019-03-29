const express = require('express');
const router = express.Router();

const UssdMenu = require('ussd-menu-builder');
const menu = new UssdMenu();

// USSD routes
router.get('/', (req, res) => {
    // res.render('ussd', res.locals.commonData);
    res.render('ussd.jade');
});

router.post('/', (req, res) => {
    menu.state('registration', {
        run: () =>{
            menu.con('Welcome to the registration system. \n Enter your username');
        },
        next: {
            '*[a-zA-Z]+': 'registration.name'
        }
    });
    
    menu.state('registration.name', {
        run: () => {
            let name = menu.val;
            let session = getSession(menu.args.sessionId);
            session.set('name', name);
            menu.con('Enter your email');
        },
        next: {
            '*\\w+@\\w+\\.\\w+': 'registration.email'
        }
    });

    menu.state('registration.email', {
        run: () => {
            let email = menu.val;
            let session = getSession(menu.args.sessionId);
            session.set('email', email);
            menu.end("Congratulations. You have successfully been registered into the system. \n You'll be hearing from us soon.");
        }
    });
    return menu;
});


// router.post('/', (req, res) => {
//     // Read variables sent via POST from the AT SDK
//     const { sessionId, serviceCode, phoneNumber, text } = req.body;

//     // split the various levels of the user input
//     const level = req.body.text.split('*');

//     let response = '';
//     if (!!text) {
//         if (text == '') {
//             // This is the first request
//             response = `CON Welcome to the registration portal. 
//                             \n Please enter your desired username`;
//         } else if ( !!level[0] && level[0] !== "" && !level[1] ) {
//             // Business logic for first level response
//             response = `CON Hi ${level[0]}, enter your email.`;
//         } else if ( !!level[1] && level[1] !== "" && !level[3] ) {
//             // Business logic for second level response
//             const data = [
//                 {"username": level[0]},
//                 {"email": level[1]}
//             ];
//             // This is the terminal request.
//             response = `END Thank you ${level[0]} for registering.
//                             \n We will keep you updated.`;
//         } 

//         // Print the response onto the page so that the AT SDK can read it
//         res.set('Content-Type: text/plain');
//         res.send(response);
//         // DONE!!!
//     }     
// });

module.exports = router;