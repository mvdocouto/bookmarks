module.exports = {
	database: "bookmark",
	username: "",
	password: "",
	params: {
		dialect: "sqlite",
		storage: "bookmarks.sqlite",
		define: {
			undescored: true
		}
	}
	jwtSecret: "b44km1rk-1P3",
	jwtSession: {session: false}
};