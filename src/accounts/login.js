const db = `./sessions/db.json`;

return account => {
	account.state('login.invalidPIN', {
		run: () => {
			account.con(`Invalid PIN provided. Try again.`);
		},
		next: {
			'*\\d{4}': 'dashboard'
		},
		defaultNext: 'login.invalidPIN'
	});
	
	module.exports = router;
	return account;
};