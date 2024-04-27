"use client";

import React, { useState } from 'react';
import GridSizeInput from '../../components/GridSizeInput.client';
import GridDisplay from '../../components/GridDisplay';

const HomePage: React.FC = () => {
  const [gridSize, setGridSize] = useState<number | null>(null);
  const [gridData, setGridData] = useState(null);

  // Fetch grid data based on the grid size
  const fetchGridData = async () => {
    try {
      const response = await fetch(`/api/grid?size=${gridSize}`);
      if (response.ok) {
        const data = await response.json();
        console.log('Grid data:', data.grid);
        setGridData(data.grid);
      } else {
        console.error('Error fetching grid data:', response.statusText);
      }
    } catch (error) {
      console.error('There was an error fetching the grid data:', error);
    }
    try {
      const response = await fetch('10.225.149.255', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        }
      });

      if (response.ok) {
        const data = await response.json();
        alert(`Data: ${JSON.stringify(data)}\nStatus: ${response.status}`);
      } else {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
    } catch (error) {
      console.error('Error:', error);
      alert('Failed to send data.');
    }
  };

  const handleSubmit = async () => {
    
  };

  // Collect and log aid units
  const handleAidSubmission = () => {
    const aidUnits = parseInt(prompt('Enter the available aid units:') ?? '0', 10);
    if (!isNaN(aidUnits)) {
      console.log(aidUnits);
    } else {
      alert('Please enter a valid number.');
    }
  };

  return (
    <div>
      <h1>Welcome to Ihsan</h1>
      <GridSizeInput onSizeSubmit={(size: number) => {
        setGridSize(size);
        setGridData(null); // Ensure grid data is cleared when size is changed
      }} />
      {gridSize && <GridDisplay size={gridSize} />}
      <button onClick={fetchGridData}>Export Grid Data</button>
      {gridData && (
        <>
          <pre>{JSON.stringify(gridData, null, 2)}</pre>
          <button onClick={handleSubmit}>Submit Grid Data</button>
        </>
      )}
      <button onClick={handleAidSubmission}>Enter Aid Available</button>
    </div>
  );
};

export default HomePage;
