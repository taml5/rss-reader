import Channel from "./Channel.tsx";
import {useCallback, useEffect, useState} from "react";
import Toolbar from "./Toolbar.tsx";
import TrackedCard from "./TrackedCard.tsx";


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
        }, 1.8e6);

        return () => clearInterval(interval);
    }, [])

    return (
        <>
            <h1>Dingbat</h1>
            <Toolbar refreshFeed={refreshFeed}/>
            <TrackedCard channels={channels} refreshFeed={refreshFeed}/>
            <div className={"feed"}>
                {channels.map(channel => {
                    return <Channel key={channel.rss_url}
                                    given_name={channel.given_name}
                                    title={channel.title}
                                    url={channel.url}
                                    rss_url={channel.rss_url}
                                    description={channel.description}
                                    stories={channel.stories}/>
                    }
                )}
            </div>
        </>
    )
}

export default App
