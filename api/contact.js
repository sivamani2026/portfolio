const { Resend } = require('resend');

const resend = new Resend(process.env.RESEND_API_KEY);

export default async function handler(req, res) {
  // Only allow POST requests
  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Method Not Allowed' });
  }

  try {
    const { name, email, message, _honey } = req.body;

    // 1. Honeypot Check (Spam Protection)
    if (_honey) {
      // Silently drop the request for bots
      return res.status(200).json({ message: 'Success' });
    }

    // 2. Validation
    if (!name || typeof name !== 'string' || name.trim() === '') {
      return res.status(400).json({ message: 'Name is required' });
    }
    if (!email || typeof email !== 'string' || email.trim() === '' || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      return res.status(400).json({ message: 'Valid email is required' });
    }
    if (!message || typeof message !== 'string' || message.trim() === '') {
      return res.status(400).json({ message: 'Message is required' });
    }
    if (message.length > 5000) {
      return res.status(400).json({ message: 'Message is too long (max 5000 characters)' });
    }

    const cleanName = name.trim();
    const cleanEmail = email.trim();
    const cleanMessage = message.trim();

    // 3. Send Email via Resend
    const { data, error } = await resend.emails.send({
      from: 'Portfolio Contact Form <onboarding@resend.dev>',
      to: 'mannemsivamani44@gmail.com',
      reply_to: cleanEmail,
      subject: `New Portfolio Message from ${cleanName}`,
      text: `Name: ${cleanName}\nEmail: ${cleanEmail}\n\nMessage:\n${cleanMessage}`
    });

    console.log("Contact API request received");
    console.log("Resend result:", { data, error });

    if (error) {
      console.error('Resend Error:', error);
      return res.status(500).json({ success: false, message: 'Failed to send message' });
    }

    return res.status(200).json({ success: true, message: 'Message sent successfully.' });
  } catch (error) {
    console.error('Server Error:', error);
    return res.status(500).json({ success: false, message: 'Internal Server Error' });
  }
}
