import React from 'react';
import styles from './Square.module.css';

interface SquareProps {
  isPerson: boolean;
  health: number;
  age: number;
}

const Square: React.FC<SquareProps> = ({ isPerson, health, age }) => {
  const handleClick = () => {
    console.log(`Clicked cell - isPerson: ${isPerson}, Health: ${health}, Age: ${age}`);
    alert(`Person: ${isPerson}\nHealth: ${health}\nAge: ${age}`);
  };

  return (
    <div
      className={`${styles.square} ${isPerson ? styles.isPerson : styles.noPerson}`}
      onClick={handleClick}
    />
  );
};

export default Square;

