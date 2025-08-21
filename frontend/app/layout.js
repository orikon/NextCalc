// app/layout.tsx

import './globals.css';

export default function RootLayout({ children }) {
    return (
      <html lang="en">
        <body>
          <main className="flex min-h-screen flex-col justify-between">
            {children}
          </main>
        </body>
      </html>
    );
  }
  