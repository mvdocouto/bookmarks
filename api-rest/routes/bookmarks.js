module.exports = app => {
	const Bookmarks = app.db.models.Bookmarks;
	const Users = app.db.models.Users;
	app.route("/bookmarks")
	    .all(app.auth.authenticate())
		.get((req, res) => {
			Bookmarks.findAll({ where: { UserId: req.user.id }})
			.then(result => res.json(result))
			.catch(error => {
				res.status(400).json({msg: error.message});
			});
		})
		.post((req, res) => {
			req.body.UserId = req.user.id;
			Bookmarks.create(req.body)
			.then(result => res.status(201).json(result))
			.catch(error => {
				res.status(400).json({msg: error.message});
			});
		});

	app.route("/bookmarks/all")
		.all(app.auth.authenticate())
		.get((req, res) => {
			Users.findById(req.user.id)
			.then(user => {
				if(user.permission){
					Users.findAll({atributes: ["id","name","email","permission"], include: [Bookmarks]})
					.then(result => {
						res.json(result);
					});
				}else{
					res.sendStatus(400)
				}
			})
			.catch(error => {
				res.status(400).json({msg: error.message});
			});
		});
	
	app.route("/bookmark/:id")
		.all(app.auth.authenticate())
		.get((req, res) => {
			console.log(req.params.id)
			Bookmarks.findOne({where: {id: req.params.id, UserId: req.user.id}})
			.then(result => {
				if(result){
					res.json(result);
				}else{
					res.sendStatus(404);
				}
			})
			.catch(error => {
				res.status(400).json({msg: error.message});
			});

		})
		.put((req, res) => {
			Bookmarks.update(req.body, {where: {id: req.params.id, UserId: req.user.id}})
			.then(result => res.sendStatus(204))
			.catch(error => {
				res.status(400).json({msg: error.message})
			});

		})
		.delete((req, res) => {
			Bookmarks.destroy({where: {id: req.params.id, UserId: req.user.id}})
			.then(result => res.sendStatus(204))
			.catch(error =>{
				res.status(400).json({msg: error.message})
			});
		});
};