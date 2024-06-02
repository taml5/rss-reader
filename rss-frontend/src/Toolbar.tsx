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


    return (<>
            <p>Refresh stories: <button onClick={prop.refreshFeed}>Refresh</button></p>
            <form onSubmit={changeCap}>
                <p>Number of stories per channel:
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
                </p>
                <button type="submit">Submit</button>
            </form>
        </>
    )
}

export default Toolbar
