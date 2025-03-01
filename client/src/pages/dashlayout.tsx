import { Outlet } from "react-router";

import logo from '../../public/logo.png'

function DashLayout() {
return (
    <div className="container grid grid-cols-2">
        <div className="sidebar w-2/5 h-[100vh] p-4" style={{borderRight: "1px solid black"}}>
            <div className="brand h-[5%] mb-4 flex flex-row justify-center items-center">
                <img src={logo} className="w-[40%] h-[100%] object-contain m-0" />
                <span className="font-medium text-3xl text-stone-700 mr-[30%] mt-2">beam</span>
            </div>

            <div className="side-items">
                <ul>
                    <li id="home-item">
                        <i></i>
                        <span>Home</span>
                    </li>
                        <li id="settings-item">
                        <i></i>
                        <span>Settings</span>
                    </li>
                </ul>
            </div>

        </div>
        <div className="content"><Outlet/></div>
    </div>

  );
}

export default DashLayout;
