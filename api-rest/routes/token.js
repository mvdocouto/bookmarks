import jwt from "jwt-simple"

module.exports = app => {
	const config = app.libs.config;
	const Users = app.db.models.Users;
	app.post("/auth", (req, res) =>{
		if(req.body.email && req.body.password){
			Users.findOne({where: {email: email }})
			.then(user => {
				if(Users.isPassword(user.password, password)){
					const payload = {id: user.id};
					res.json({
						token: jwt.encode(payload, config.jwtSecret)
					});
				}else{
					res.senStatus(401);
				}
			})
			.catch(error => res.sendStatus(401));
		}else{
			res.sendStatus(401);
		}
	});
};