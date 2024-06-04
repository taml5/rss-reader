import Channel from "./Channel.tsx";
import {useCallback, useEffect, useState} from "react";
import Options from "./Options.tsx";
import Feed from "./Feed.tsx";
import './App.scss';

function App() {
    const [channels, setChannels] = useState<Channel[]>([]);
    const refreshFeed = useCallback( () => {
        const url: string = "http://127.0.0.1:5000/";
        fetch(url, {method: "GET"}).then(r => {
            if (r.ok) {
                return r.json();}
        }).then((data) => {
            console.log("Fetched channels" + data.map(
                (channel: Channel) => {return " " + channel.title})
            );
            setChannels(data);
        }).catch((error: Error) => console.log(error))
    }, [setChannels]);

    useEffect(() => {
        refreshFeed()
    }, [setChannels])

    useEffect(() => {
        const interval = setInterval(() => {
            refreshFeed();
            console.log("Refreshed feed");
        }, 600000);

        return () => clearInterval(interval);
    }, [])

    return (
        <>
            <div id={"header"}>
                <h1>Dingbat</h1>
                <button id={"refreshButton"} onClick={refreshFeed}>Refresh Channels</button>
            </div>
            <div className={"app"}>
                <Options channels={channels} refreshFeed={refreshFeed}/>
                <Feed channels={channels}/>
            </div>
        </>
    )
}

export default App
