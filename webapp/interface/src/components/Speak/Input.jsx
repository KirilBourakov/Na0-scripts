import { useState } from 'react';

export default function Input({sending, setSending, state}){
    const [typedTranscript, setTypedTranscript] = useState('');

    function handleSubmit(e){
        e.preventDefault()
        setSending(true)
        if (state.connected){
            state.connection.emit('userSpeech',  {'transcript': typedTranscript})
            state.connection.on('finishedSpeaking', () => {
                console.log("done speaking")
                setSending(false)
            })
        } else {
            console.error('Cannot send without connection; Error in Speak.')
        } 
    }

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