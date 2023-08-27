"use client"
import Link from 'next/link'
import React from 'react'
import styles from './navbar.module.css'

const links=[
    {
        id:0,
        title:"Home",
        url:"/"
    },
    {
        id:2,
        title:"Blog",
        url:"/blog"
    },
    {
        id:1,
        title:"About",
        url:"/about"
    },
    {
        id:3,
        title:"Contact",
        url:"/contact"
    },
    {
        id:4,
        title:"Portfolio",
        url:"/portfolio"
    },
    {
        id:5,
        title:"Dashboard",
        url:"/dashboard"
    },
]

function Navbar() {
  return (
    <div className={styles.container}>
        <Link href='/' className={styles.logo}>Daily Blog</Link>
        <div className={styles.links}>
            {
               links.map((ob)=>{
                return(
                    <Link href={ob.url} key={ob.id} className={styles.link}>{ob.title}</Link>
                )
               })
            }
            <button 
                className={styles.logout}
                onClick={()=>{
                    console.log("logged out");
                }}
            >
                Logout
            </button>
        </div>
    </div>
  )
}

export default Navbar