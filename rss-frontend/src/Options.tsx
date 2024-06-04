import Toolbar from "./Toolbar.tsx";
import TrackedContainer from "./TrackedContainer.tsx";
import Channel from "./Channel.tsx";
import './Options.scss';

interface IOptions {
    refreshFeed: () => void
    channels: Channel[]
}

function Options(prop: IOptions) {
    return <div id={"options"}>
                <Toolbar refreshFeed={prop.refreshFeed}/>
                <TrackedContainer channels={prop.channels} refreshFeed={prop.refreshFeed}/>
    </div>
}

export default Options;
