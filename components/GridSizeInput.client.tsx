
"use client";

import React, { useState, FormEvent } from 'react';

interface GridSizeInputProps {
  onSizeSubmit: (size: number) => void;
}

const GridSizeInput: React.FC<GridSizeInputProps> = ({ onSizeSubmit }) => {
  const [size, setSize] = useState<string>('');

  const handleSubmit = (event: FormEvent) => {
    event.preventDefault();
    const gridSize = parseInt(size, 10);
    if (!isNaN(gridSize) && gridSize > 0) {
      onSizeSubmit(gridSize);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="number"
        value={size}
        onChange={(e) => setSize(e.target.value)}
        placeholder="Enter grid size"
        min="1"
      />
      <button type="submit">Create Grid</button>
    </form>
  );
};

export default GridSizeInput;

