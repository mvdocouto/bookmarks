import fs from "fs";
import path from "path";
import Sequelize from "sequelize";

let db = null;

module.exports = app => {
	if(!db){
		// Chamando as configuraoes de banco
		const config = app.libs.config;
		// Criando o objeto de coenxao
		const sequelize = new Sequelize(
			config.database,
			config.username,
			config.password,
			config.params
		);
		db = {
			sequelize,
			Sequelize,
			models: {}
		}
		// linkando as atulizacoes entre db e model
		const dir = path.join(__dirname, "models");
		fs.readdirSync(dir).forEach(file => {
			const modelDir = path.join(dir, file);
			const model = sequelize.import(modelDir);
			db.models[model.name] = model;
		});
		// fazendo o relacionamento entre as tabelas
		Object.keys(db.models).forEach(key => {
			db.models[key].associate(db.models);
		});
	}
	return db;
};