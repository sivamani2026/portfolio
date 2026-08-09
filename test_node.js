process.env.RESEND_API_KEY = 're_1234567890'; // Mock key
const handler = require('./api/contact.js');

const req = {
  method: 'POST',
  body: {
    name: 'Ram Charan',
    email: 'mannemsivamani44@gmail.com',
    message: 'hiii'
  }
};

const res = {
  status: function(code) {
    this.statusCode = code;
    return this;
  },
  json: function(data) {
    console.log("MOCK RES STATUS:", this.statusCode);
    console.log("MOCK RES JSON:", data);
    return this;
  }
};

async function run() {
  console.log("Starting test...");
  try {
    await handler(req, res);
  } catch(e) {
    console.error("Test execution threw error:", e);
  }
}

run();
