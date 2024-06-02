import Toolbar from "./Toolbar.tsx";
import TrackedCard from "./TrackedCard.tsx";
import Channel from "./Channel.tsx";
import './Options.scss';

interface IOptions {
    refreshFeed: () => void
    channels: Channel[]
}

function Options(prop: IOptions) {
    return <div className={"options"}>
                <Toolbar refreshFeed={prop.refreshFeed}/>
                <TrackedCard channels={prop.channels} refreshFeed={prop.refreshFeed}/>
    </div>
}

export default Options;
