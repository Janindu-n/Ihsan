
"use client";

import React, { useState } from 'react';
import GridSizeInput from '../../components/GridSizeInput.client';
import GridDisplay from '../../components/GridDisplay';

const HomePage: React.FC = () => {
  const [gridSize, setGridSize] = useState<number | null>(null);
  const [gridData, setGridData] = useState(null);

  const fetchGridData = async () => {
    try {
      const response = await fetch(`/api/exportGrid?size=${gridSize}`);
      if (response.ok) {
        const data = await response.json();
        console.log('Grid data:', data.grid);
        // Set the grid data in the state if you want to do something with it on the page
        setGridData(data.grid);
      } else {
        console.error('Error fetching grid data:', response.statusText);
      }
    } catch (error) {
      console.error('There was an error fetching the grid data:', error);
    }
  };
  

  return (
    <div>
      <h1>Welcome to Ihsan</h1>
      <GridSizeInput onSizeSubmit={(size: number) => setGridSize(size)} />
      {gridSize && <GridDisplay size={gridSize} />}
      <button onClick={fetchGridData}>Export Grid Data</button>
      {/* Render your grid data here */}
    </div>
  );
};

export default HomePage;
