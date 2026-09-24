const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');

function readJson(rel) {
  const filePath = path.join(root, rel);
  try {
    return JSON.parse(fs.readFileSync(filePath, 'utf8'));
  } catch (err) {
    throw new Error(`Failed to parse ${rel}: ${err.message}`);
  }
}

function assertFile(rel) {
  const filePath = path.join(root, rel);
  if (!fs.existsSync(filePath)) {
    throw new Error(`Missing file: ${rel}`);
  }
}

console.log('[dice-party] validating project structure...');

const app = readJson('app.json');
readJson('project.config.json');
readJson('sitemap.json');

if (!Array.isArray(app.pages) || app.pages.length < 3) {
  throw new Error('app.json should declare at least three pages');
}

console.log(`[dice-party] found ${app.pages.length} pages: ${app.pages.join(', ')}`);

for (const page of app.pages) {
  assertFile(`${page}.json`);
  assertFile(`${page}.wxml`);
  assertFile(`${page}.wxss`);
  assertFile(`${page}.js`);
  console.log(`[dice-party] ✓ ${page}`);
}

assertFile('utils/mock-data.js');
console.log('[dice-party] ✓ utils/mock-data.js');

console.log('[dice-party] validation passed ✓');
