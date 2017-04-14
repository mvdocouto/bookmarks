module.exports = {
    database: "bookmark",
    username: "",
    password: "",
    params: {
        dialect: "sqlite",
        storage: "bookmarks-test.sqlite",
        logging: false,
        define: {
            underscored: true
        }
    },
    jwtSecret: process.env.JWT_SECRET || "b44km1rk-1P3",
    jwtSession: {session: false}
};