import Channel from "./Channel.tsx";
import {useEffect, useState} from "react";


function App() {
    const [channels, setChannels] = useState<Channel[]>([]);

    useEffect(() => {
        let channels: Channel[] = [];

        const url: string = "http://127.0.0.1:5000";
        fetch(url).then(r => {
            if (r.ok) {
                return r.json();}
        }).then((data) => {
            for (let i = 0; i < data.length; i++) {
                channels.push(data[i]);
            }
            setChannels(channels);
        }).catch((error: Error) => console.log(error))

    }, [setChannels])

    return (
        <>
            <h1>Dingbat</h1>
            <div className={"feed"}>
                {channels.map(channel => {
                    return <Channel key={channel.rss_url}
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
