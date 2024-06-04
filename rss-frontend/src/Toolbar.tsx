import React from "react";

interface IToolbar {
    refreshFeed: () => void;
}


function Toolbar(prop: IToolbar) {
    function changeCap(event: React.FormEvent<HTMLFormElement>) {
        event.preventDefault();  // prevent browser from reloading the page

        const form = event.currentTarget;
        const formData = new FormData(form);

        fetch('http://127.0.0.1:5000/storyCap/', {method: "PUT", body: formData})
            .then(() => {
                console.log("Updated story limit to " + formData.get("num"));
                prop.refreshFeed();
            })
    }


    return (<div id={"toolbar"}>
            <form onSubmit={changeCap}>
                <p>Number of stories per channel:</p>
                <label>
                    <input type={"radio"} name={"num"} value={3}/>
                    3
                </label>
                <label>
                    <input type={"radio"} name={"num"} value={5}/>
                    5
                </label>
                <label>
                    <input type={"radio"} name={"num"} value={10}/>
                    10
                </label>
                <button type="submit">Change</button>
            </form>
        </div>
    )
}

export default Toolbar
