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
app.get("/api/score/:mode/:difficulty/:username", (req, res) => {
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

//POST request to validate login information with server
app.post('/api/login', (req, res) => {
    const username = req.body.username;
    const password = req.body.password;

    try {
    const storedLogin = JSON.parse(fs.readFileSync(path.resolve('login', username + '.json'), 'utf8'));
        if(storedLogin.password == password){
            res.status(200).send("success");
        }
        else{
            res.status(404).send("password mismatch")
        }
    } catch (err) {
        console.log(err);
     res.status(404).send("no such user");
    }

});

//POST request to create new user
app.post('/api/register', (req, res) => {
    const username = req.body.username;
    const password = {"password": req.body.password};

    try {
        const temp = fs.readFileSync(path.resolve('login', username + '.json'), 'utf8');
        res.status(404).send("user already exists");
    } catch (err) {
        fs.writeFile(path.resolve('login', username + '.json'), JSON.stringify(password), (err1) => {
        if (err1){
            console.log(err1);
            res.status(500).send("error creating new user");
        }
        else {
          res.status(200).send("new user created");
        }
        });
    }

});



/**
 * Server Activation
 */
 app.listen(port, () => {
  console.log(`Listening to requests on http://localhost:${port}`);
});