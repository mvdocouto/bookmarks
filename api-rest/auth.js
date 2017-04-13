import passport from "passport";
import {Strategy} from "passport-jwt";
import {ExtractJwt} from "passport-jwt";

module.exports = app => {
	const Users = app.db.models.Users;
	const config = app.libs.config;
	var options = {};
    options.jwtFromRequest = ExtractJwt.fromAuthHeader();
    options.secretOrKey = config.jwtSecret;
	const strategy = new Strategy(options,
		(payload, done) => {
			Users.findById(payload.id)
			.then(user => {
				if(user){
					return done(null, {
						id: user.id,
						email: user.email
					});
				}
				return done(null, false);
			})
			.catch(error => done(error, null));
		});
	passport.use(strategy);
	return {
		initilize: () => {
			return passport.initilize();
		},
		authenticate: () => {
			return passport.authenticate("jwt", config.jwtSession)
		}
	};	
};
