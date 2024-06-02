import Channel from "./Channel.tsx";
import React from "react";

interface ITracked {
    channels: Channel[]
    refreshFeed: () => void
}


function TrackedCard(prop: ITracked) {
    function trackChannel(event: React.FormEvent<HTMLFormElement>) {
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
        <div>
            <h2>Tracked Channels</h2>
            <div>
                {prop.channels.map(channel => {
                    return <div key={channel.rss_url} className={"trackedChannel"}>
                        <p>{channel.given_name}: {channel.rss_url}</p>
                        <button onClick={() => untrackChannel(channel.given_name)}>Untrack</button>
                    </div>
                })}
            </div>
            <form onSubmit={trackChannel}>
                <p>Add channel:</p>
                <label>
                    Name:
                    <input name={"name"} />
                </label>
                <label>
                    URL:
                    <input name={"url"} />
                </label>
                <button type="submit">Submit</button>
            </form>
        </div>
    )
}

export default TrackedCard
