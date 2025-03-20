import { useState } from 'react';
import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition';

export default function Speak(){
    const [sending, setSending] = useState("")


    const {
        transcript,
        listening,
        resetTranscript,
        browserSupportsSpeechRecognition
    } = useSpeechRecognition();

    if (!browserSupportsSpeechRecognition) {
        return <span>Browser doesn't support speech recognition.</span>;
    }

    async function finish(){
        SpeechRecognition.stopListening() 
        setSending(true)

        // get response from server
        let response = await fetch("http://127.0.0.1:5001/speech",
        {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            method: "POST",
            body: JSON.stringify({
                'transcript': transcript
            })
        })
        response = await response.json()
        console.log(response['response'])

        resetTranscript()
        setSending(false)
    }

    return (
        <div className="flex flex-col items-center justify-center">
            <h1 className='font-bold text-xl text-center'>Speak</h1>
            <hr className='py-2 mx-2 w-full'/>

            <div>
                <p>Microphone:&nbsp;
                    {listening ? <strong className='text-green-500'>ON</strong> : <strong className='text-red-500'>OFF</strong>}    
                </p>

                <button 
                    onClick={() => listening ? finish(): SpeechRecognition.startListening()}
                    className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full'
                    disabled={sending}
                >
                    {listening ? 'Stop' : 'Start'}
                </button>

                <p>{sending ? "Await the Nao's response." : ""}</p>
            </div>
        </div>
    )
}