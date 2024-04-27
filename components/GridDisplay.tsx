"use client";
import Square from './Square';


interface GridDisplayProps {
  size: number;
}

const GridDisplay: React.FC<GridDisplayProps> = ({ size }) => {
  const createGridArray = (size: number) => {
    return Array.from({ length: size }, () =>
      Array.from({ length: size }, () => ({
        is_person: Math.random() > 0.5,
        health: Math.floor(Math.random() * 100),
        age: Math.floor(Math.random() * 100),
      }))
    );
  };

  const gridArray = createGridArray(size);

  const gridStyle = {
    display: 'grid',
    gridTemplateColumns: `repeat(${size}, 50px)`,
    gridGap: '2px',
  };

  return (
    <div style={gridStyle}>
      {gridArray.map((row, rowIndex) =>
        row.map((cell, cellIndex) => (
          <Square
            key={`${rowIndex}-${cellIndex}`}
            isPerson={cell.is_person}
            health={cell.health}
            age={cell.age}
          />
        ))
      )}
    </div>
  );
};

export default GridDisplay;
