import Channel from "./Channel.tsx";
import React, {useState} from "react";

interface ITracked {
    channels: Channel[]
    refreshFeed: () => void
}


function TrackedContainer(prop: ITracked) {
    const [channelName, setChannelName] = useState("");
    const [channelURL, setChannelURL] = useState("");

    function trackChannel(event: React.FormEvent<HTMLFormElement>) {
        setChannelName("");
        setChannelURL("");
        event.preventDefault();  // prevent browser from reloading the page

        const form = event.currentTarget;
        const formData = new FormData(form);

        fetch('http://127.0.0.1:5000/channels/', {method: "POST", body: formData})
            .then(() => {
                console.log("Added channel " + formData.get("name") + ", url: " + formData.get("url"));
                prop.refreshFeed();
            })
    }

    function untrackChannel(name: string) {
        fetch('http://127.0.0.1:5000/channels/', {method: "DELETE", body: name})
            .then(() => {
                console.log("Untracked channel " + name);
                prop.refreshFeed();
            })
    }

    return (
        <div id={"trackedChannels"}>
            <h2>Tracked Channels</h2>
            <form id="channelAdder" onSubmit={trackChannel}>
                <h3>Add channel</h3>
                <label>
                    <p>
                        {"Name:  "}
                        <input name={"name"}
                           value={channelName}
                           onChange={e => setChannelName(e.target.value)}/>
                    </p>
                </label>
                <label>
                    <p>
                        {"URL:  "}
                        <input name={"url"}
                           value={channelURL}
                           onChange={e => setChannelURL(e.target.value)}/>
                    </p>
                </label>
                <button type="submit">Submit</button>
            </form>
            <div id={"tracked"}>
                {prop.channels.map(channel => {
                    return <div key={channel.rss_url} className={"trackedChannel"}>
                        <p>{channel.given_name}</p>
                        <p><small><small>{channel.rss_url}</small></small></p>
                        <button onClick={() => untrackChannel(channel.given_name)}>Untrack</button>
                    </div>
                })}
            </div>
        </div>
    )
}

export default TrackedContainer
