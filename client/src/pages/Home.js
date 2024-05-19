import React, { useEffect, useRef, useState } from 'react'
import { PageCounter } from '../components/PageCounter'
import { GET_CITATIONS_ENDPOINT, GET_MESSAGES_ENDPOINT, HEADERS } from '../constants';
import { MessageCard } from '../components/MessageCard';
import css from '../css/Home.css';
import { CircularLoadingIndicator } from '../components/CircularLoadingIndicator';

export const Home = () => {
    const [num, setNum] = useState(1);
    const firstRender = useRef(true);
    const [messages, setMessages] = useState([]);
    const [citations, setCitations] = useState(null);
    const [loading, setLoading] = useState(false);

    const fetchMessages = async () => {
        try {
            const response = await fetch(
                `${GET_MESSAGES_ENDPOINT}?page=${num}`,
                {
                    method: 'GET',
                    headers: HEADERS
                }
            );
            if(response.ok) {
                const responseData = await response.json();
                setMessages(responseData.data.data);
            }
        } catch(err) {
            console.error(err);
        }
    }

    const fetchCitations = async () => {
        setLoading(true);
        try {
            const response = await fetch(
                GET_CITATIONS_ENDPOINT,
                {
                    method: 'POST',
                    headers: HEADERS,
                    body: JSON.stringify({messages})
                }
            );
            if(response.ok) {
                const responseData = await response.json();
                console.log(responseData);
                setCitations(responseData);
            }
        } catch(err) {
            console.error(err);
        } finally {
            setLoading(false);
        }

    }

    useEffect(() => {
        if(firstRender.current) {
            firstRender.current = false;
        }
        else {
            fetchMessages();
            setCitations(null);
        }
    }, [num])

  return (
    <div className='homepage'>
        <h1 className='homepage--title'>📝 Citation Finder</h1>
        <div className='homepage--form'>
        <PageCounter num={num} setNum={setNum}/>
        <button
            className='button counter--get-citation-btn'
            onClick={fetchCitations}    
        >Get Citations</button>
        {loading && <CircularLoadingIndicator/>}
        <div className='message-result'>
            <h1>💬 Messages</h1>
            {
                messages.map((message, idx) => {
                    return <MessageCard
                        id={message.id}
                        response={message.response}
                        citations={(citations && citations[idx].length!==0) ? citations[idx].citations : null}
                    />
                })
            }
        </div>
        </div>
    </div>
  )
}
