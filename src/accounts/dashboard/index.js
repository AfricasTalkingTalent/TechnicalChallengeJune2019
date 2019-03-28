const lodash = require('lodash');
const jsonfile = require('jsonfile');

const db = `./sessions/db.json`;

const dashboardInstructions = `Choose a service to proceed: \n1. Deposit money \n2. Check savings \n3. View statement`;

// return account => {
// 	account.state('dashboard', {
// 		run: () => {
// 			const {
// 				val,
// 				args: { phoneNumber }
// 			} = account;

// 			const data = JSONFile.readFileSync(db);
// 			let user = data[`${phoneNumber}`];

// 			JSONFile.writeFileSync(db, {
// 				...data,
// 				users: _.map(data.users, user => {
// 					const { phone } = user;

// 					if (phone === phoneNumber) {
// 						return { ...user, page: 0 };
// 					}

// 					return user;
// 				})
// 			});

// 			if (_.isEqual(user, {})) {
// 				user = _.find(data.users, ({ phone }) => phone === phoneNumber);
// 				const { authenticated, lastState } = user;

// 				if (typeof authenticated !== 'undefined') {
// 					account.con(dashboardInstructions);
// 				} else if (`${user.pin}` === `${val}`) {
// 					JSONFile.writeFileSync(db, {
// 						...data,
// 						users: _.map(data.users, user => {
// 							const { phone } = user;

// 							if (phone === phoneNumber) {
// 								return { ...user, authenticated: true };
// 							}

// 							return user;
// 						})
// 					});

// 					account.con(dashboardInstructions);
// 				} else {
// 					account.go('login.invalidPIN');
// 				}
// 			} else {
// 				if (`${user.pin}` === `${val}`) {
// 					JSONFile.writeFileSync(db, {
// 						...data,
// 						users: _.concat(data.users, [{ ...user, phone: phoneNumber }]),
// 						[`${phoneNumber}`]: {}
// 					});

// 					account.con(dashboardInstructions);
// 				} else {
// 					account.end(`PINs don't match`);
// 				}
// 			}
// 		},
// 		next: {
// 			'1': 'dashboard.deposit',
// 			'2': 'dashboard.savings',
// 			'3': 'dashboard.statements'
// 		}
// 	});

// 	_.over([deposit, savings, statements])(account);

// 	return account;
// };
// module.exports = router;