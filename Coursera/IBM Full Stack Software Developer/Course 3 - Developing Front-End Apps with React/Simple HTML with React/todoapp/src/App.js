import axios from 'axios';
import React, {useState, useEffect} from "react";

const App = (props)=> {
    //define the state and the setter
    const [APIlist, setAPIlist] = useState();

    //On load invoke method to genrate list
    useEffect(() => {
        let url = "https://api.publicapis.org/entries?category=Animals";
        axios({
          method: 'get',
          url: url,
          responseType: 'json'
        }).then(resp => {
            let listOfEntries = resp.data.entries;
            let listOfEntriesAsArray = Object.entries(listOfEntries);
            let i=1;
            let entryDetails = listOfEntriesAsArray.map((entryDetail)=>{
              return(
                <tr key={i++}>
                  <td key={i++} style={{color: "red",border: "1px solid black"}}>{entryDetail[1]["API"]} </td>
                  <td key={i++} style={{color: "red",border: "1px solid black"}}>{entryDetail[1]["Link"]} </td>
                </tr>)
            })
            setAPIlist(entryDetails);
          })
        .catch(err => {
            console.log(err.toString())
        });
    }, []);

    const colorStyle = { color:props['color'], fontSize:props['size']}

    return (
        <div>
            <h2>APIs List</h2>
            <br/>

            <div style={colorStyle}><ul>{APIlist}</ul></div>
        </div>
);
}

export default App;
