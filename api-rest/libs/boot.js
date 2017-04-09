module.exports = app => {
	app.db.sync().done(() => {
		app.listen(app.get("port"), () => {
			console.log(`Bookmark API - porta ${app.get("port")}`)
		});
	});
}