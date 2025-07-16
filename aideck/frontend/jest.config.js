module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'jsdom',
  moduleFileExtensions: ['ts', 'tsx', 'js', 'jsx'],
  transform: {
    '^.+\\.(ts|tsx)$': 'ts-jest',
  },
  testMatch: [
    '../../tests/frontend/**/*.test.(ts|tsx)',
    '**/src/**/*.test.(ts|tsx)'
  ],
  setupFiles: ['<rootDir>/jest.setup.js'],
};
