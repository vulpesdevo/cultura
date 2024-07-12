
//RUN THIS CODE FIRST IN TERMINAL TO INSTALL DEPENDENCIES
//npm install express nodemailer body-parser express-session 

import express from "express";
import nodemailer from "nodemailer";
import bodyParser from "body-parser";
import session from "express-session";
const app = express();
const PORT = 5173;

app.use(bodyParser.json());
app.use(express.static('public')); // Serve static files from the "public" directory

app.use(session({
    secret: 'your-secret-key',
    resave: false,
    saveUninitialized: true,
    cookie: { secure: false } // Set to true in production with HTTPS
}));

app.post('/send-otp', (req, res) => {
    const { email } = req.body;
    const otp = Math.floor(100000 + Math.random() * 900000).toString(); // Generate a 6-digit OTP

    // Store OTP in session
    req.session.otp = otp;
    req.session.email = email;

    // Configure the email transport using the default SMTP transport and a Gmail account
    const transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
            user: 'culturalink62@gmail.com',
            pass: 'syhj wqky hzwz kllz'
        }
    });

    const mailOptions = {
        from: 'culturalink62@gmail.com',
        to: email,
        subject: 'Your OTP Code',
        text: `Your OTP code is ${otp}`
    };

    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            console.error('Error sending OTP:', error);
            return res.status(500).json({ success: false, message: 'Error sending OTP' });
        }
        res.json({ success: true, message: 'OTP sent' });
    });
});

app.post('/verify-otp', (req, res) => {
    const { email, otp } = req.body;
    console.log('Received OTP for verification:', otp);
    if (req.session.otp === otp && req.session.email === email) {
        console.log('OTP verified successfully');
        return res.json({ success: true, message: 'OTP verified successfully' });
    }
    console.error('Invalid OTP');
    res.status(400).json({ success: false, message: 'Invalid OTP' });
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
