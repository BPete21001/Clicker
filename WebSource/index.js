// index.js

/**
 * Required External Modules
 */
const express = require("express");
const path = require("path");
const fs = require("fs");
/**
 * App Variables
 */
const app = express();
const port = process.env.PORT || "8000";

/**
 *  App Configuration
 */
app.use(express.json());

/**
 * Routes Definitions
 */
app.get("/", (req, res) => {
  res.status(200).send("Clicker");
});

//GET call to see a score for a specific user
app.get("/api/leaderboard/:mode/:difficulty/:username", (req, res) => {
  const username = req.params.username;
  const mode = req.params.mode;
  const difficulty = req.params.difficulty;

  try {
    const data = fs.readFileSync(path.resolve('scores', String(mode), String(difficulty), username + '.json'), 'utf8');
    res.status(200).send(data);
    } catch (err) {
     res.status(404).send("No score found for mode: " + mode + ", difficulty: " + difficulty + ", user: " + username);
    }
});

//POST call to add a new score to the server
app.post('/api/newscore', (req, res) => {
    const difficulty = req.body.difficulty;
    const username = req.body.username;
    const mode = req.body.mode;
    const score = {
        "score": req.body.score,
        "time" : req.body.time
    }

    fs.writeFile(path.resolve('scores', mode, difficulty, username + '.json'), JSON.stringify(score), (err) => {
    if (err){
      console.log(err);
        res.status(500).send("Error writing score");
    }
    else {
      res.status(200).send("Score Posted");
    }
    });

});


/**
 * Server Activation
 */
 app.listen(port, () => {
  console.log(`Listening to requests on http://localhost:${port}`);
});