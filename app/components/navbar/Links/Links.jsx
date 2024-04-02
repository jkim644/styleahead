"use client";

import styles from "./links.module.css";
import NavLink from "./navLink/navLink";
import { useState } from "react";

const links = [ 
    { 
        title: "Closet",
        path: "/closet",
    }, 
    { 
        title: "About",
        path: "/about",
    },
    { 
        title: "Contact", 
        path: "/contact", 
    }
];

const Links = () => { 

    const[open, setOpen] = useState(false);

    return(
        <div className={styles.container}>
        <div className={styles.links}>
            {links.map((link=>(
                <NavLink item={link} key={link.title}/>
            )))}

        </div>
            <button className={styles.menuButton} onClick={()=>setOpen(prev=>!prev)}>Menu</button>
            { 
                open && <div className={styles.mobileLinks}>
                    {links.map((link) => (
                        <NavLink item={link} key={link.title}/>
                    ))}
                    
                    </div>
            }
        </div>

    )
}

export default Links