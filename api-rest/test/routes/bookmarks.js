import jwt from "jwt-simple";

describe("Routes: Bookmarks", () => {
    const Users = app.db.models.Users;
    const Bookmarks = app.db.models.Bookmarks;
    const jwtSecret = app.libs.config.jwtSecret;
    let token;
    let adminToken;
    let fake_bookmark;

    beforeEach(done => {
        Users
            .destroy({where: {}})
            .then(() => Users.create({
                name: "Usuario de Teste",
                email: "teste@teste.com",
                password: "1234"
            }))
            .then(user => {
                Bookmarks
                    .destroy({where: {}})
                    .then(() => Bookmarks.bulkCreate([{
                        id: 1,
                        name: "Bookmark 1",
                        url: "http://bookmark1.com",
                        UserId: user.id
                    }, {
                        id: 2,
                        name: "Bookmark 2",
                        url: "http://bookmark2.com",
                        UserId: user.id
                    }]))
                    .then(bookmarks => {
                        fake_bookmark = bookmarks[0];
                        token = jwt.encode({id: user.id}, jwtSecret);
                    })
                    .then(() => Users.create({
                        name: "Admininistrador",
                        email: "adm@teste.com",
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
        describe("status 200", () => {
            it("returns a list of bookmarks", done => {
                request.get("/bookmarks")
                    .set("Authorization", `JWT ${token}`)
                    .expect(200)
                    .end((err, res) => {
                        expect(res.body).to.have.length(2);
                        expect(res.body[0].name).to.eql("Bookmark 1");
                        expect(res.body[1].name).to.eql("Bookmark 2");
                        done(err);
                    });
            });
        });
    });

    describe("POST /bookmarks", () => {
        describe("status 200", () => {
            it("creates a new bookmarks", done => {
                request.post("/bookmarks")
                    .set("Authorization", `JWT ${token}`)
                    .send({name: "Node JS", url: "http://nodejs.com/"})
                    .expect(201)
                    .end((err, res) => {
                        expect(res.body.name).to.eql("Node JS");
                        expect(res.body.url).to.eql("http://nodejs.com/");
                        done(err);
                    });
            });
        });
    });

    describe("GET /bookmark/:id", () => {
        describe("status 200", () => {
            it("returns one bookmark", done => {
                request.get(`/bookmark/${fake_bookmark.id}`)
                    .set("Authorization", `JWT ${token}`)
                    .expect(200)
                    .end((err, res) => {
                        expect(res.body.name).to.eql("Bookmark 1");
                        done(err);
                    });
            });
        });
        describe("status 404", () => {
            it("throws error when bookmark not exist", done => {
                request.get("/bookmark/0")
                    .set("Authorization", `JWT ${token}`)
                    .expect(404)
                    .end((err, res) => done(err));
            });
        });
    });

    describe("PUT /bookmark/:id", () => {
        describe("status 204", () => {
            it("updates a bookmark", done => {
                request.put(`/bookmark/${fake_bookmark.id}`)
                    .set("Authorization", `JWT ${token}`)
                    .send({
                        name: "Java Script",
                    })
                    .expect(204)
                    .end((err, res) => done(err));
            });
        });
    });

    describe("DELETE /bookmark/:id", () => {
        describe("status 204", () => {
            it("removes a bookmark", done => {
                request.delete(`/bookmark/${fake_bookmark.id}`)
                    .set("Authorization", `JWT ${token}`)
                    .expect(204)
                    .end((err, res) => done(err));
            });
        });
    });

    describe("GET /bookmarks/all", () => {
        describe("status 200", () => {
            it("admin gets a list of bookmarms grouped by user", done => {
                request.get('/bookmarks/all')
                    .set("Authorization", `JWT ${adminToken}`)
                    .expect(200)
                    .end((err, res) => done(err));
            });
        });
        describe("status 400", () => {
            it("not an admin gets error", done => {
                request.get('/bookmarks/all')
                    .set("Authorization", `JWT ${token}`)
                    .expect(400)
                    .end((err, res) => done(err));
            });
        });
    });
});