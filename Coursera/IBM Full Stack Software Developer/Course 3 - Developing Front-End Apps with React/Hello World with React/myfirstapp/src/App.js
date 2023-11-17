function App(props) {
    const currDate = new Date();

    return (
        <div>
            <h1>Gary Siu!</h1>
            <h2>
                It is {currDate.toLocaleDateString()} the time now 
                is {currDate.toLocaleTimeString()}.
            </h2>
        </div>
    );
}

export default App;
