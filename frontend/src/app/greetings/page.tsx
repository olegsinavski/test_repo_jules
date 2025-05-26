// src/app/greetings/page.tsx
import React from 'react';

export default function GreetingsPage() {
  const [greetings, setGreetings] = React.useState<string[]>([]);
  const [loading, setLoading] = React.useState(true);
  const [error, setError] = React.useState<string | null>(null);

  React.useEffect(() => {
    async function fetchGreetings() {
      try {
        setLoading(true);
        const response = await fetch('/api/greetings');
        if (!response.ok) {
          throw new Error(`Error: ${response.statusText}`);
        }
        const data = await response.json();
        setGreetings(data.greetings || []);
      } catch (err) {
        if (err instanceof Error) {
          setError(err.message);
        } else {
          setError('An unknown error occurred');
        }
      } finally {
        setLoading(false);
      }
    }

    fetchGreetings();
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-4">
      <main className="max-w-2xl w-full bg-white shadow-md rounded-lg p-8">
        <h1 className="text-3xl font-bold text-center text-gray-800 mb-6">Greetings</h1>
        {loading && <p className="text-center text-gray-600">Loading greetings...</p>}
        {error && <p className="text-center text-red-500">Error loading greetings: {error}</p>}
        {!loading && !error && greetings.length === 0 && (
          <p className="text-center text-gray-600">No greetings available at the moment.</p>
        )}
        {!loading && !error && greetings.length > 0 && (
          <ul className="list-disc pl-5 space-y-2">
            {greetings.map((greeting, index) => (
              <li key={index} className="text-lg text-gray-700">
                {greeting}
              </li>
            ))}
          </ul>
        )}
      </main>
    </div>
  );
}
