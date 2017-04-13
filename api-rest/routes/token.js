import jwt from "jwt-simple"

module.exports = app => {
	const config = app.libs.config;
	const Users = app.db.models.Users;
	app.post("/auth", (req, res) => {
		if(req.body.email && req.body.password){
			const email = req.body.email
			const password = req.body.password
			Users.findOne({where: {email: email}})
			.then(user => {
				if(Users.isPasswordCorrect(user.password, password)){
					const payload = {id: user.id};
					res.json({
						token: jwt.encode(payload, config.jwtSecret)
					});
				}else{
					res.senStatus(400).json({msg: error.message});
				}
			})
			.catch(error => res.sendStatus(400).json({msg: error.message}));
		}else{
			res.sendStatus(400);
		}
	});
};