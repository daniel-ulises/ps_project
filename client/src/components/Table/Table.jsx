export default function Table({ procs }) {

    // The processes are mapped and formatted for the table.
    const procItems = procs.map(item => {
        return (
            <tr key={item.pk}>
                <td>{item.fields["uid"]}</td>
                <td>{item.fields["user"]}</td>
                <td>{item.fields["pid"]}</td>
                <td>{item.fields["cmd"]}</td>
            </tr>
        )
    })

    return (
    <table>
        <thead>
            <tr>
                <th>UID</th>
                <th>USER</th>
                <th>PID</th>
                <th>CMD</th>
            </tr>
        </thead>
        <tbody>    
            {
                // If there is any process in the variable, it will
                // display the mapped processes. If not, it will display "loading..."
                procs.length > 0 ? procItems : "Loading..."
                
            }
        </tbody>

    </table>
    )
}