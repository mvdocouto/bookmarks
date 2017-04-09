module.exports = app => {
	return {
		findAll: (params, callback) => {
			return callback([
				{name: "Zeca"},
				{name: "Paulo"}	
			]);
		}
	};	
};