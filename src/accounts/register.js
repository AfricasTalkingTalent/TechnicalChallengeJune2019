const lodash = require('lodash');
const jsonfile = require('jsonfile');

const db = `./sessions/db.json`;

return account => {
	account.state('register', {
		run: () => {
			const {
				val,
				args: { phoneNumber }
			} = account;

			const data = jsonfile.JSONFile.readFileSync(db);

			jsonfile.JSONFile.writeFileSync(db, {
				...data,
				[`${phoneNumber}`]: {
					username: val
				}
			});

			account.con(`Enter your email:`);
		},
		next: {
			'*\\w+': 'register.pin'
		}
	});

  account.state('register.pin', {
		run: () => {
			const {
				val,
				args: { phoneNumber }
			} = account;

			const data = jsonfile.JSONFile.readFileSync(db);

			jsonfile.JSONFile.writeFileSync(db, {
				...data,
				[`${phoneNumber}`]: {
					...data[`${phoneNumber}`],
					email: val
				}
			});

			const { username } = data[`${phoneNumber}`];

			account.con(`Hi ${username}! \nEnter your preferred 4-digit PIN:`);
		},
		next: {
			'*\\d{4}': 'register.pin.confirm'
		},
		defaultNext: 'register.pin.invalidPIN'
	});

  account.state('register.pin.invalidPIN', {
    run: () => {
      account.con(`Invalid PIN provided. Try again.`);
    },
    next: {
      '*\\d{4}': 'register.pin.confirm'
    },
    defaultNext: 'register.pin.invalidPIN'
  });

  account.state('register.pin.confirm', {
    run: () => {
      const {
        val, args: { phoneNumber }
      } = account;

      const data = jsonfile.JSONFile.readFileSync(db);

      jsonfile.JSONFile.writeFileSync(db, {
        ...data,
        [`${phoneNumber}`]: {
          ...data[`${phoneNumber}`],
          pin: val
        }
      });

      const { username } = data[`${phoneNumber}`];

      account.con(`Hi ${username}! \nEnter your preferred 4-digit PIN again:`);
    },
    next: {
      '*\\d{4}': 'dashboard'
    },
    defaultNext: 'register.pin.invalidPIN'
  });

	module.exports = router;
  return account;
};
