import type { NextApiRequest, NextApiResponse } from 'next';

const createGridData = (size: number) => {
  return Array.from({ length: size }, () =>
    Array.from({ length: size }, () => ({
      is_person: Math.random() > 0.5,
      health: Math.floor(Math.random() * 100),
      age: Math.floor(Math.random() * 100),
    }))
  );
};

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method === 'GET') {
    // Extract size from query parameters. Default size is 5 if not specified.
    const size = parseInt(req.query.size as string) || 5;
    const gridData = createGridData(size);
    res.status(200).json({ grid: gridData });
    console.log('Grid data:', gridData);
  } else {
    res.setHeader('Allow', ['GET']);
    res.status(405).end(`Method ${req.method} Not Allowed`);
  }
}
