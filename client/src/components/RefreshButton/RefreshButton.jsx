export default function RefreshButton({ getData })  {
    // The button refreshes the data, filling the database with
    // the most recent processes and the displaying them in the table
    return (
        <button onClick={() => getData()} >
            Refresh
        </button>
    )

}