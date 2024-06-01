import { Story } from "./Channel.tsx";

function StoryCard(prop: Story) {
    return (
        <a id={prop.guid} className="story" href={prop.link} target="_blank">
            <h3>{prop.title}</h3>
            <p>{prop.description}</p>
        </a>
    );
}

export default StoryCard
