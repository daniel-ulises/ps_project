import { useEffect } from "react"

export default function FilterTable ({ users, getUsers, getById }) {

    // As soon as the 'select' element loads, it will 
    // get the users that can be used to filter the table
    useEffect(() => {
        getUsers();
    }, [])

    // The users are mapped, creating one option for each user.
    const user = users.map(user => {
        return <option value={user.fields["uid"]} key={user.pk}>{user.fields["user"]}</option>
    })

    return (
        
        <div className="filter-container">
            <p>Filter by user</p>
            {/* When a user is selected it executes the 'getById' function, filtering the table. */}
            <select name="users" onChange={id => getById(id.target["value"])}>
                {users ? user : "hi"}
            </select>
        </div>
    )
}