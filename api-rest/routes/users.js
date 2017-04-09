module.exports = app => {
	// Get data from Models
	const Users = app.models.users;
	app.get("/users", (req, res) => {
		Users.findAll({}, (users)  => {
			res.json({users: users})
		}); 
	});
};