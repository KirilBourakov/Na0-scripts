import { useState } from 'react';
import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition';
import { useConnectContext } from '../../state/connectionState'; 
import Input from './Input';
import Recognition from './Recognition';


export default function Speak(){
    const [sending, setSending] = useState("")
    const {state, setState} = useConnectContext();

    const {
        transcript,
        listening,
        resetTranscript,
        browserSupportsSpeechRecognition
    } = useSpeechRecognition();

    if (!browserSupportsSpeechRecognition) {
        return <Input sending={sending} setSending={setSending} state={state}/>
    }

    return <Recognition 
        sending={sending}
        setSending={setSending}
        state={state}
        listening={listening}
        transcript={transcript}
        resetTranscript={resetTranscript}  
    />
}