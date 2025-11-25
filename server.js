const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Database setup
const db = new sqlite3.Database('./contacts.db', (err) => {
    if (err) {
        console.error('Error opening database ' + err.message);
    } else {
        console.log('Connected to the SQLite database.');
        db.run(`CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            message TEXT,
            date TEXT
        )`, (err) => {
            if (err) {
                console.error('Error creating table ' + err.message);
            }
        });
    }
});

// Routes
app.post('/api/contact', (req, res) => {
    const { name, email, message } = req.body;
    const date = new Date().toISOString();

    if (!name || !email || !message) {
        return res.status(400).json({ error: 'Please provide all fields' });
    }

    const sql = `INSERT INTO contacts (name, email, message, date) VALUES (?, ?, ?, ?)`;
    db.run(sql, [name, email, message, date], function(err) {
        if (err) {
            return res.status(500).json({ error: err.message });
        }
        res.json({
            message: 'Contact saved successfully',
            id: this.lastID
        });
    });
});

app.get('/api/contacts', (req, res) => {
    const sql = `SELECT * FROM contacts ORDER BY date DESC`;
    db.all(sql, [], (err, rows) => {
        if (err) {
            return res.status(500).json({ error: err.message });
        }
        res.json({
            message: 'success',
            data: rows
        });
    });
});

// Start server
app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
