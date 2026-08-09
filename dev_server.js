process.env.RESEND_API_KEY = 're_1234567890';
const express = require('express');
const app = express();
const contactHandler = require('./api/contact.js');

app.use(express.json());

app.post('/api/contact', async (req, res) => {
    try {
        await contactHandler(req, res);
    } catch (err) {
        console.error("Express Error:", err);
        res.status(500).json({ error: "Express Error" });
    }
});

app.listen(3000, () => console.log('Listening on port 3000'));
