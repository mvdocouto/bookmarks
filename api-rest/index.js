import express from "express";
import consign from "consign";

const app = express();

consign()
.include("libs/config.js")
.then("db.js")
.then("routes")
.then("libs/middlewares.js")
.then("libs/boot.js")
.into(app)