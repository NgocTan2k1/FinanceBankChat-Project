import { useState } from "react";

export const useAnswer = (data) => {
    const [type, setType] = useState(data?.types ? data?.types : "text") // ['text', 'graph']
    const [element, setElement] = useState(data?.elements ? data?.elements : []);
    const [text, setText] = useState(data?.message ? data?.message : "");
    const [tables, setTables] = useState(data?.table ? data?.table : []);
    const [content, setContent] = useState(null);
    const processData = () => {
        if (type !== "text") {
            let message = text;
            setContent(message.split('\n -')[0]);
        } else {
            setContent(text);
        }
    }

    return {
        type,
        setType,
        element,
        setElement,
        text,
        setText,
        processData,
        setContent,
        content,
        tables,
        setTables,
    }
}