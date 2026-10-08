import React from 'react'; import './Sidebar.css'; import { useNavigate } from "react-router-dom"; import { useState } from "react";
function Sidebar() {

    const navigate = useNavigate();
    const [open, setOpen] = useState(true);

    return (

        <div className={open ? "SideBar" : "SideBar closed"}>

            <button
                className="ToggleButton"
                onClick={() => setOpen(!open)}
            >
                ☰
            </button>

            {open && (

                <>

                    <button
                        className="Buttom"
                        onClick={() => navigate("/dashboard")}
                    >
                        Home
                    </button>

                    <button
                        className="Buttom"
                        onClick={() => navigate("/recalificaciones")}
                    >
                        Recalificaciones
                    </button>


                    <button
                        className="Buttom"
                        onClick={() => navigate("/incoming")}
                    >
                        Incoming
                    </button>

                    <button
                        className="Buttom"
                        onClick={() => navigate("/scrap")}
                    >
                        Scrap
                    </button>

                    <button
                        className="Buttom"
                        onClick={() => navigate("/buscador-de-piezas")}
                    >
                        Buscador de Piezas
                    </button>

                    <button
                        className="Buttom"
                        onClick={() => navigate("/")}
                    >
                        Login
                    </button>

                </>

            )}

        </div>

    );


}
export default Sidebar;