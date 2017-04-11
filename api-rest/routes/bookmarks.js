module.exports = app => {
	// Get data from Models
	const Bookmarks = app.db.models.Bookmarks;
	app.route("/bookmarks")
		.get((req, res) => {
			Bookmarks.findAll({})
			.then(result => res.json({bookmarks: bookmarks}))
			.catch(error => {
				res.status(400).json({msg: error.message});
			});
		})
		.post((req, res) => {
			console.log(req.body);
			Bookmarks.create(req.body)
			.then(result => res.json(result))
			.catch(error => {
				res.status(400).json({msg: error.message});
			});

		});
	
	app.route("/bookmark/:id")
		.get((req, res) => {
			Bookmarks.findOne({where: req.params})
			.then( result => {
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
			Bookmarks.update(req.body, {where: req.params})
			.then(result => res.sendStatus(204))
			.catch(error => {
				res.status(400).json({msg: error.message})
			});

		})
		.delete((req, res) => {
			Bookmarks.destroy({where: req.params})
			.then(result => res.sendStatus(204))
			.catch(error =>{
				res.status(400).json({msg: error.message})
			});
		});
};