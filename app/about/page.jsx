import Image from "next/image"
import styles from "./about.module.css"
const About = () => {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      
      <div>About
        <div className = {styles.imgContainer}>
          <Image src="/decision_fatigue.png" fill></Image>
        </div>
      </div>
    </main>
  )
  }

  export default About;



    
