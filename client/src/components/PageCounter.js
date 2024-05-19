import React, { useState } from 'react'
import css from "../css/Home.css";

export const PageCounter = (props) => {
    
    const handle_increase = () => {
        props.setNum(num => num+1);
    }
    const handle_decrease = () => {
        props.setNum(num => num-1);
    }

  return (
    <div className='counter'>
        <h2>Current Page</h2>
        <div className='counter--btn-container'>
            <button
                className={`button counter-btn ${props.num <= 1 && 'disabled'}`}
                onClick={props.num > 0 ? handle_decrease : null}
                >-</button>
            <h3 className='counter--num'>{props.num}</h3>
            <button
                className='button counter-btn'
                onClick={handle_increase}    
            >+</button>
        </div>
    </div>
  )
}
