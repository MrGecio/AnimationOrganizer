import React from 'react'; import Sidebar from '../components/Sidebar/Sidebar';
function MainLayout({ children }) {
    return (

        <div style={{ display: "flex" }}>

            <Sidebar />

            <div style={{ padding: "20px" }}>

                {children}

            </div>

        </div>


    );
}
export default MainLayout;