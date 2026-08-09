const handler = require('./api/contact.js');

// Mock request and response
const req = {
  method: 'POST',
  body: {
    name: 'Test',
    email: 'test@example.com',
    message: 'Hello'
  }
};

const res = {
  status: function(code) {
    this.statusCode = code;
    return this;
  },
  json: function(data) {
    console.log("RESPONSE:", this.statusCode, data);
  }
};

async function test() {
  try {
    // If the module uses export default in CommonJS, it might be exported as handler.default or handler
    const fn = handler.default || handler;
    await fn(req, res);
  } catch (err) {
    console.error("CAUGHT ERROR:", err);
  }
}

test();
