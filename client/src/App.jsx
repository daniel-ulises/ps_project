import { useEffect, useState } from "react";
import RefreshButton from "./components/RefreshButton/RefreshButton";
import Table from "./components/Table/Table";
import FilterTable from "./components/FilterTable/FilterTable"
import axios from "axios";
import "./app.css"

export default function App() {
    const [msg, setMsg] = useState([]);
    const [procs, setProcs] = useState([]);
    const [users, setUsers] = useState([]);
    
    // Get the users that will be used in the 'select'
    // element, in order to filter the table by them.
    async function getUsers() {
        const users = await axios.get("/api/get/users");
        setUsers(users.data);
    }

    // Get specific processes by the user's UID, which is
    // passed through the parameter from the 'select' element.
    async function getUserById(id) {
        const userById = await axios.get(`/api/get/${id}`);
        setProcs(userById.data);
    }

    // Run the bash script in the backend, caching the current processes
    // and then get the cached data to display it on the table.
    async function getData()  {
        setProcs([])
        const cache = await axios.get("/api/cache");
        setMsg(cache.data);
        
        const query = await axios.get("/api/get/ps");
        setProcs(query.data);
    }

    // useEffect will run the 'getData()' function once when
    // the React App first loads.
    useEffect( () => {
        getData();
    }, [])

    console.log(users);
    return (
        <>
            <div className="container">
                <div className="refresh-button">
                    <RefreshButton getData={getData} />
                    Running processes: {procs.length}
                </div>   

                {/* The filtering 'select' element will only be displayed if there are processes available.
                    Doing it like this, prevents the 'select' element from having no options at all.
                */}
                { procs.length > 0 ? <FilterTable users={users} getUsers={getUsers} getById={getUserById} /> : null }
                
                <div className="table">
                    <Table procs={procs} msg={msg} />
                </div>
            </div>
        </>
    )
}
