import React from 'react';
import ReactLoading from 'react-loading';
import css from "../css/Home.css";

export const CircularLoadingIndicator = () => {
  return (
    <div className='circular-loading'>
        <ReactLoading type={'spin'} color={'black'} height={50} width={50} />
        <small>Our model is working hard to find your citations</small>
    </div>
  )
}
