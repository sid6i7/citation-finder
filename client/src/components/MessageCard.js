import React, { useState } from "react";
import css from "../css/Home.css";
import { CitationResult } from "./CitationResult";

export const MessageCard = (props) => {
 
  return (
    <div className="message-card">
      <h3 className="message-card--id">#{props.id}</h3>
      <p className="message-card--response">
        {props.response}
        <hr />
      </p>
      <CitationResult
        citations={props.citations}
      />
    </div>
  );
};
