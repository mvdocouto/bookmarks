module.exports = app => {
	app.listen(app.get("port"), () => {
		console.log(`Bookmark API - porta ${app.get("port")}`)
	});
}