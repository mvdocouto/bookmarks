describe("Routes: Token", () => {
    const Users = app.db.models.Users;
    describe("POST /auth", () => {
        // Criando um usuario para teste.
        beforeEach(done => {
            Users.destroy({where: {}})
                .then(() => Users.create({
                        name: "Usuario de teste",
                        email: "teste@teste.com",
                        password: "1234"
                }))
                .then(done());
        });
        // Testando o Login e o retorno do Token
        describe("status 200", () => {
            Users.findAll({});
            it("retorna o token de usuario autenticado.", done => {
                request.post("/auth")
                    .send({
                        email: "teste@teste.com",
                        password: "1234"
                    })
                    .expect(200)
                    .end((err, res) => {
                        // Verificando se um token foi retornado.
                        expect(res.body).to.include.keys("token");
                        done(err);
                    });
            });
        });
        describe("status 400", () => {
            it("retorna erro se o password estiver errado", done => {
                request.post("/auth")
                    .send({
                        email: "teste@teste.com",
                        password: "abcd"
                    })
                    .expect(400)
                    .end((err, res) => {
                        done(err);
                    });
            });
            it("retorna erro se email na existir", done => {
                request.post("/auth")
                    .send({
                        email: "desconhecido@test.com",
                        password: "1234"
                    })
                    .expect(400)
                    .end((err, res) => {
                        done(err);
                    });
            });
            it("retorna erro se o email e a senha estiverem em branco", done => {
                request.post("/auth")
                    .expect(400)
                    .end((err, res) => {
                        done(err);
                    });
            });
        });
    });
});
