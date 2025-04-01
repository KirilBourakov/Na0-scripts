import { useState } from 'react';
import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition';
import { useConnectContext } from '../state/connectionState';

export default function Speak(){
    const [sending, setSending] = useState("")
    const {state, setState} = useConnectContext();
    const [typedTranscript, setTypedTranscript] = useState('');

    const {
        transcript,
        listening,
        resetTranscript,
        browserSupportsSpeechRecognition
    } = useSpeechRecognition();

    async function finish(){
        setSending(true)
        SpeechRecognition.stopListening() 

        console.log(state)
        if (state.connected){
            state.connection.emit('userSpeech',  {'transcript': transcript})
            state.connection.on('finishedSpeaking', () => {
                console.log("done speaking")
                resetTranscript()
                setSending(false)
            })
        } else {
            console.error('Cannot send without connection; Error in Speak.')
        } 
    }

    function controlSpeech(){
        console.log(listening)
        if (listening){
            finish()
        } else {
            SpeechRecognition.startListening()
        }
    }

    function handleSubmit(){
        setSending(true)
        if (state.connected){
            state.connection.emit('userSpeech',  {'transcript': typedTranscript})
            state.connection.on('finishedSpeaking', () => {
                console.log("done speaking")
                resetTranscript()
                setSending(false)
            })
        } else {
            console.error('Cannot send without connection; Error in Speak.')
        } 
    }

    if (!browserSupportsSpeechRecognition) {
        return (
            <div>
                <span>Browser doesn't support speech recognition.</span> 
                <form onSubmit={handleSubmit}>
                <div>
                    <label>Input via text:</label>
                    <input
                    type="text"
                    value={typedTranscript}
                    onChange={(e) => setTypedTranscript(e.target.value)}
                    required
                    />
                </div>
                <button type="submit">Submit</button>
                </form>
            </div>
        )
    }

    return (
        <div className="flex flex-col items-center justify-center">
            <h1 className='font-bold text-xl text-center'>Speak</h1>
            <hr className='py-2 mx-2 w-full'/>

            <div>
                <p>Microphone:&nbsp;
                    {listening ? <strong className='text-green-500'>ON</strong> : <strong className='text-red-500'>OFF</strong>}    
                </p>

                {listening ? 
                    <button 
                        onClick={finish}
                        className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full'
                        disabled={sending}
                    >
                        Stop
                    </button>
                    :
                    <button 
                        onClick={SpeechRecognition.startListening}
                        className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full'
                        disabled={sending}
                    >
                        Start
                    </button>
                }
                

                <p>{sending ? "Await the Nao's response." : ""}</p>
            </div>
        </div>
    )
}