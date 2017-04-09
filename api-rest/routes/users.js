module.exports = app => {
	// Get data from Models
	const Users = app.models.users;
	app.route("/users")
		.all((req, res) => {
			delete req.body.id;
			next();
		})
		.get((req, res) => {
			Users.findAll({})
			.then(result => res.json({users: users}))
			.catch(error => {
				res.status(412).json({msg: error.message});
			});
		})
		.post((req, res) => {
			Users.create(req.body)
			.then(result = res.json(result))
			.catch(error => {
				res.status(412).json({msg: error.message});
			});

		});
	
	app.route("/users/:id")
		.all((req, res) => {
			delete req.body.id;
			next();
		})
		.get((req, res) => {
			Users.findOne({where: req.params})
			.then( result => {
				if(result){
					res.json(result);
				}else{
					res.sendStatus(404);
				}
			})
			.catch(error => {
				res.status(412).json({msg: error.message});
			});

		})
		.put((req, res) => {
			Users.update(req.body, {where: req.params})
			.then(result => res.sendStatus(204))
			.catch(error => {
				res.status(412).json({msg: error.message})
			});

		})
		.delete((req, res) => {
			Users.destroy({where: req.params})
			.then(result => res.sendStatus(204))
			.catch(error =>{
				res.status(412).json({msg: error.message})
			});
		});
};