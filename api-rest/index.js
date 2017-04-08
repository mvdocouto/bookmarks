import express from "express";
const PORT = 3000;

const app = express();
app.get("/", (req, res) => res.json({status: "Bookmark API"}));
app.listen(PORT, () => console.log('Bookmark API - porta {$PORT}'));
