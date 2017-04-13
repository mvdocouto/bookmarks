module.exports = app => {
	
	const Users = app.db.models.Users;
	
	// app.route("/user/:id")
 //        .all(app.auth.authenticate())
    app.route("/user/:id")
        .get((req, res) => {
            Users.findById(req.params.id, {
                attributes: ["id", "name", "email", "permission"]
         	})
        	.then(result => res.json(result))
            .catch(error => {
                res.status(400).json({msg: error.message});
            });
        })
        .put((req, res) => {
            Users.update(req.body, {where: {id: req.params.id} })
            .then(result => res.sendStatus(204))
            .catch(error => {
                res.status(400).json({msg: error.message});
            });
        })
        .delete((req, res) => {
            Users.destroy({where: {id: req.params.id} })
            .then(result => res.sendStatus(204))
            .catch(error => {
                res.status(400).json({msg: error.message});
            });
        });

    app.route("/users")
        .post((req, res) => {
            Users.create(req.body)
            .then(result => res.json(result))
            .catch(error => {
                res.status(400).json({msg: error.message});
            });
        });

    app.route("/users")
        .get((req, res) => {
            Users.findAll({
                attributes: ["id", "name", "email", "permission"]
            })
            .then(result => res.json(result))
            .catch(error => {
                res.status(400).json({msg: error.message});
            });
        });


   	app.route("/users/all")
        .get((req, res) => {
            Users.findAll({})
            .then(user => {
                if(user.isAdmin){
                    Users.findAll({
                        attributes: ["id", "name", "email", "permission"]
                    })
                    .then(result => res.json(result));
                }else{
                    res.sendStatus(400);
                }
            })
            .catch(error => {
                res.status(400).json({msg: error.message});
            });
        });    
}