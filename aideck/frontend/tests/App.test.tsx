import { render, screen } from '@testing-library/react';
import App from '../src/App';

test('renders AIDECK app', () => {
  render(<App />);
  expect(screen.getByText(/AIDECK/i)).toBeInTheDocument();
});
