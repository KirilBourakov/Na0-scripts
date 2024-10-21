import express from "express";
import { spawn } from "child_process";

const app = express();
const port = 3000;

let pythonProcess = null;

app.get('/', (req, res) => {
  pythonProcess = spawn('C:\\Users\\alexb\\Desktop\\na0\\.env\\python.exe', ['../walk_and_talk.py'])
  pythonProcess.stdout.on('data', (data) => {
    console.log(`Python stdout: ${data}`);
  });
  res.send('Started Python process!');
});

app.get('/kill', (req, res) => {
  pythonProcess.kill('SIGKILL')
  pythonProcess.stdout.on('data', (data) => {
    console.log(`Python stdout: ${data}`);
  });
  res.send('Killed Python process!');
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});