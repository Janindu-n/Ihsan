import type { NextApiRequest, NextApiResponse } from 'next';

const createGridData = (size: number) => {
  return Array.from({ length: size }, () =>
    Array.from({ length: size }, () => {
      const is_person = Math.random() > 0.5;
      return {
        is_person: is_person,
        health: is_person ? Math.floor(Math.random() * 100) : 0,
        age: is_person ? Math.floor(Math.random() * 100) : 0,
      };
    })
  );
};

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method === 'GET') {
    const size = parseInt(req.query.size as string) || 5;
    const gridData = createGridData(size);
    res.status(200).json({ grid: gridData });
  } else {
    res.setHeader('Allow', ['GET']);
    res.status(405).end(`Method ${req.method} Not Allowed`);
  }
}
