import { Resend } from 'resend';

const resend = new Resend(process.env.RESEND_API_KEY);

export const config = {
  runtime: 'edge', // Explicitly use the Edge runtime for Web APIs
};

export default async function handler(req) {
  if (req.method !== 'POST') {
    return Response.json({ success: false, message: 'Method Not Allowed' }, { status: 405 });
  }

  try {
    const body = await req.json();
    const { name, email, message, _honey } = body;

    if (_honey) {
      return Response.json({ success: true, message: 'Success' }, { status: 200 });
    }

    if (!name || typeof name !== 'string' || name.trim() === '') {
      return Response.json({ success: false, message: 'Name is required' }, { status: 400 });
    }
    if (!email || typeof email !== 'string' || email.trim() === '' || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      return Response.json({ success: false, message: 'Valid email is required' }, { status: 400 });
    }
    if (!message || typeof message !== 'string' || message.trim() === '') {
      return Response.json({ success: false, message: 'Message is required' }, { status: 400 });
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
      return Response.json(
        { success: false, message: "Failed to send message." },
        { status: 500 }
      );
    }

    console.log("RETURNING SUCCESS");
    return Response.json(
      { success: true, message: "Message sent successfully." },
      { status: 200 }
    );
  } catch (error) {
    console.error('Server Error:', error);
    return Response.json(
      { success: false, message: 'Internal Server Error' },
      { status: 500 }
    );
  }
}
