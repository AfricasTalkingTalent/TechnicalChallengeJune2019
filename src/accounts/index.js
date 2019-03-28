const UssdMenu = require('ussd-menu-builder');
const lodash = require('lodash');
const jsonfile = require('jsonfile');

const login = require('./login');
const register = require('./register');
const dashboard = require('./dashboard/index');

var account = new UssdMenu();

const db = `./sessions/db.json`;

// return () => {
	account.startState({
		run: () => {
			const { phoneNumber } = account.args;

			const data = jsonfile.JSONFile.readFileSync(db);

			jsonfile.JSONFile.writeFileSync(db, {
				...data,
				users:
					lodash._.map(data.users, user => {
						const { phone } = user;

						if (phone === phoneNumber) {
							return {
								...lodash._.pick(
									user,
									lodash._.remove(lodash._.keys(user), key => key !== 'authenticated')
								),
								page: 0
							};
						}

						return user;
					}) || [],
				[`${phoneNumber}`]: {}
			});

			const registerInstructions = `Welcome. Enter your desired uername to register:`;

			if (typeof data.users !== 'undefined') {
				const user = lodash._.find(data.users, ({ phone }) => phone === phoneNumber);

				if (typeof user !== 'undefined') {
					account.con(
						`Welcome back, ${user.username}! \nEnter your 4-digit PIN to continue:`
					);
				} else {
					account.con(registerInstructions);
				}
			} else {
				account.con(registerInstructions);
			}
		},
		next: {
			'*\\d{4}': 'dashboard',
			'*\\w+': 'register'
		}
	});

	account.state('invalidOption', {
		run: () => {
			account.end(`Invalid option`);
		}
	});

	lodash._.over([login.login, register.register, dashboard.dashboard])(account);

	return account;
// };
module.exports = router;