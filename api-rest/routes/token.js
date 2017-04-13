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
				const payload = {id: user.id};
				res.json({
					token: jwt.encode(payload, config.jwtSecret)
				});
				// console.log(user.password);
				// console.log(password);
				// console.log(Users.isPasswordCorrect(user.password, password));
				// if(Users.isPasswordCorrect(user.password, password)){
				// 	console.log(user.id);
				// 	const payload = {id: user.id};
				// 	res.json({
				// 		token: jwt.encode(payload, config.jwtSecret)
				// 	});
				// }else{
				// 	res.senStatus(400).json({msg: error.message});
				// }
			})
			.catch(error => res.sendStatus(400));
		}else{
			res.sendStatus(400);
		}
	});
};