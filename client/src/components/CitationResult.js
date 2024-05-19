import React, { useState } from 'react'
import { CitationCard } from './CitationCard';
import css from "../css/Home.css";

export const CitationResult = (props) => {
    const [showSources, setShowSources] = useState(true);
    const displayCitations = () => {
        if (props.citations) {
          if (props.citations.length === 0) {
            return (
              <div className="source-card--no-citation">No Citations Found</div>
            );
          } else {
            return (
              <div>
                <h3>Citations</h3>
                <button
                  onClick={() => setShowSources(!showSources)}
                  className="button message-card--sources-btn"
                >
                  {showSources ? "Hide" : "Show"}
                </button>
                {showSources && (
                  <div className="source-card--container">
                    {props.citations.map((citation) => {
                      return <CitationCard id={citation.id} link={citation.link} />;
                    })}
                  </div>
                )}
              </div>
            );
          }
        } else {
          return "Get Citations First";
        }
    }
  return (
    <div>
        {displayCitations()}
    </div>
  )
}
