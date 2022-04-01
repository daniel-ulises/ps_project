export default function Table({ procs }) {
    const procItems = procs.map(item => {
        return (
            <tr>
                <td>{item.uid}</td>
                <td>{item.user}</td>
                <td>{item.pid}</td>
                <td>{item.cmd}</td>
            </tr>
        )
    })

    return (
    <table>
        <tr>
            <th>UID</th>
            <th>USER</th>
            <th>PID</th>
            <th>CMD</th>
        </tr>
            { procs[0] ? procItems : <p>Nothing to show here</p> }

    </table>
    )
}