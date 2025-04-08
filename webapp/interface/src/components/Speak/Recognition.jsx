export default function Recognition({sending, setSending, state, transcript, listening, resetTranscript}){
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