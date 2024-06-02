export interface Story {
    title: string
    description: string
    link?: string
    guid?: string
}

function StoryCard(prop: Story) {
    return (
        <div id={prop.guid} className="story">
            <h3>{prop.title}</h3>
            <p>{prop.description}</p>
            <a href={prop.link} target="_blank"> <small>more</small> </a>
        </div>
    );
}

export default StoryCard
