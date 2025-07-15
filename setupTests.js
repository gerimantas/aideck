require('@testing-library/jest-dom');

// TextEncoder polifyll Node aplinkai (pvz. react-router)
if (typeof global.TextEncoder === 'undefined') {
  global.TextEncoder = require('util').TextEncoder;
}
