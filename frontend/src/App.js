import "./App.css";
import Header from "./components/header";
import Main from "./components/main";

function App() {
    return (
        <div className="bg-bg-clr p-[50px] min-h-screen h-full">
            <div className="flex justify-center">
                <Header />
            </div>
            <div className="flex justify-center">
                <Main />
            </div>
        </div>
    );
}

export default App;
