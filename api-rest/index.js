import express from "express";
import consign from "consign";

const app = express();

consign()
.include("models")
.then("routes")
.then("libs/middlewares.js")
.then("libs/boot.js")
.into(app)