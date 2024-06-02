import Channel from "./Channel.tsx";
import './Feed.scss';

interface IFeed {
    channels: Channel[]
}

function Feed(prop: IFeed) {
    return (<div className={"feed"}>
                {prop.channels.map(channel => {
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
    );
}

export default Feed;
