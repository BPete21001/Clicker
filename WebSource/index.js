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
app.get("/api/getscore/:username", (req, res) => {
  const username = req.params.username;


  try {
    const data = fs.readFileSync(path.resolve('scores', username + '.json'), 'utf8');
    res.status(200).send(data);
    } catch (err) {
     res.status(500).send("No score found for user: " + username);
    }
});

//POST call to add a new score to the server
app.post('/api/newscore/:username', (req, res) => {
    const newScore = JSON.stringify(req.body);
    const username = req.params.username;

    
    fs.writeFile(path.resolve('scores', username + '.json'), String(newScore),  (err) => {
        if (err)
        res.status(500).send("Error writing score");
        else {
        console.log("Successful Post")
      }
    
    });

    res.status(200).send('Score Posted');
});


/**
 * Server Activation
 */
 app.listen(port, () => {
  console.log(`Listening to requests on http://localhost:${port}`);
});