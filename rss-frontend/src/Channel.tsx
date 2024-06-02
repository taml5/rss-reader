import StoryCard from "./StoryCard.tsx";

export interface Story {
    title: string
    description: string
    link?: string
    guid?: string
}

interface Channel {
    title: string
    url: string
    rss_url: string
    description: string
    stories: Story[]
}

function Channel(channel: Channel) {
    return (<div className={"channelCard"}>
        <h2>{channel.title}</h2>
        <p>{channel.description}</p>
        <div className={"storyContainer"}>
            {channel.stories.map(story =>
                <StoryCard key={story.guid + story.title}
                           title={story.title}
                           description={story.description}
                           link={story.link}
                />
            )}
        </div>
    </div>);
}

export default Channel;
