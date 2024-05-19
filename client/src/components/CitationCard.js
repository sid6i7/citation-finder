import React from "react";

export const CitationCard = (props) => {
  return (
    <div className="source-card">
      <h3 className="source-card--id">#{props.id}</h3>
      <div className="source-card--link">
        {props.link ? <a className="source-card--link" href={props.link}>{props.link}</a> : "No Link"}
      </div>
    </div>
  );
};
