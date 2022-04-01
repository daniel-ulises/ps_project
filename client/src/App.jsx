import { useEffect, useState } from "react";
import RefreshButton from "./components/RefreshButton/RefreshButton";
import Table from "./components/Table/Table";
import axios from "axios";

export default function App() {
    const [msg, setMsg] = useState([]);
    const [procs, setProcs] = useState([]);
    
    async function getProcs()  {
        const cache = await axios.get("http://127.0.0.1:8000/api/cache");
        setMsg(cache.data)
        
        const query = await axios.get("http://127.0.0.1:8000/api/get");
        setProcs(query.data)
    }

    useEffect(() => {
        getProcs();
    }, [])

    console.log(procs);
    return (
        <>
            <h1>Current Processes Running</h1>
            <div className="container">
                <div className="refresh-button">
                    <RefreshButton getProcs={getProcs} />
                </div>
                <div className="table">
                    <Table procs={procs} />
                </div>
            </div>
        </>
    )
}
