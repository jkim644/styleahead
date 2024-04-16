import styles from "./closet.module.css"
import Image from "next/image"

const Closet = () => {
    return (
      <main>
        <div className={styles.container}>Closet
          <div className={styles.textContainer}>
            <h1>Style Ahead Closet</h1>
            <p>Hi</p>
            <div className={styles.buttons}>
              <button className = {styles.button}>Add new item</button>
              <button className = {styles.button}>Remove item </button>
              <button className = {styles.button}>Generate outfit</button>
              <button className = {styles.button}>Generate schedule </button>
            </div>
            <div className={styles.brands}>
              <Image src="/clothing_robot.png" fill className={styles.brandImg}></Image>
            </div>
          </div>
          <div className={styles.imgContainer}>
            <Image src="/Analytics.gif"></Image>
          </div>
        </div>
      </main>
    )
    }
  
    export default Closet;