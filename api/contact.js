const { Resend } = require('resend');

const resend = new Resend(process.env.RESEND_API_KEY);

module.exports = async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ success: false, message: 'Method Not Allowed' });
  }

  try {
    const { name, email, message, _honey } = req.body || {};

    if (_honey) {
      return res.status(200).json({ success: true, message: 'Success' });
    }

    if (!name || typeof name !== 'string' || name.trim() === '') {
      return res.status(400).json({ success: false, message: 'Name is required' });
    }
    if (!email || typeof email !== 'string' || email.trim() === '') {
      return res.status(400).json({ success: false, message: 'Valid email is required' });
    }
    if (!message || typeof message !== 'string' || message.trim() === '') {
      return res.status(400).json({ success: false, message: 'Message is required' });
    }

    const cleanName = name.trim();
    const cleanEmail = email.trim();
    const cleanMessage = message.trim();

    console.log("CONTACT API START");
    console.log("REQUEST BODY:", { name: cleanName, email: cleanEmail, message: cleanMessage });

    const { data, error } = await resend.emails.send({
      from: 'Portfolio Contact Form <onboarding@resend.dev>',
      to: 'mannemsivamani44@gmail.com',
      reply_to: cleanEmail,
      subject: `New Portfolio Message from ${cleanName}`,
      text: `Name: ${cleanName}\nEmail: ${cleanEmail}\n\nMessage:\n${cleanMessage}`
    });

    console.log("RESEND DATA:", data);
    console.log("RESEND ERROR:", error);

    if (error) {
      console.error("RESEND ERROR:", error);
      console.log("RETURNING ERROR");
      return res.status(500).json({ success: false, message: "Failed to send message." });
    }

    console.log("RETURNING SUCCESS");
    return res.status(200).json({ success: true, message: "Message sent successfully." });
  } catch (error) {
    console.error('Server Error:', error);
    return res.status(500).json({ success: false, message: 'Internal Server Error' });
  }
};
