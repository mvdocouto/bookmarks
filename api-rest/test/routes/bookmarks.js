import jwt from "jwt-simple";

describe("Routes: Bookmarks", () => {
    const Users = app.db.models.Users;
    const Bookmarks = app.db.models.Bookmarks;
    const jwtSecret = app.libs.config.jwtSecret;
    let token;
    let adminToken;
    let fakeBookmark;

    beforeEach(done => {
        // Criando um usuario fake
        Users.destroy({where: {}})
        .then(() => Users.create({
            name: "Usurario de teste",
            email: "teste@teste.com",
            password: "1234"
        }))
        .then(user => {
            // Criando Bookmarks Fake
            Bookmarks.destroy({where: {}})
            .then(() => Bookmarks.bulkCreate([{
                id: 1,
                title: "bookmark 1",
                url: "http://www.bookmark1.com/",
                user_id: user.id
            }, {
                id: 2,
                title: "Bookmark 2",
                url: "http://www.bookmark2.com",
                user_id: user.id
            }]))
            .then(bookmarks => {
                fakeBookmark = bookmarks[0];
                token = jwt.encode({id: user.id}, jwtSecret);
            })
            .then(() => Users.create({
                name: "Administrador",
                email: "admin@teste.com",
                permission: true,
                password: "adm@1234"
            }))
            .then(user => {
                adminToken = jwt.encode({id: user.id}, jwtSecret);
                done();
            });
        });
    });

    describe("GET /bookmarks", () => {
        
    });

    describe("POST /bookmarks", () => {
        
    });

    describe("GET /bookmarks/all", () => {
              
    });

    describe("GET /bookmark/:id", () => {
        
    });

    describe("PUT /bookmark/:id", () => {
        
    });

    describe("DELETE /bookmark/:id", () => {
        
    });

    
});