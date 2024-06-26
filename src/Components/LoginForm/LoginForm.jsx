import React from 'react'
import "./LoginForm.css"
import {FaUser} from "react-icons/fa"
import {FaLock} from "react-icons/fa"

const LoginForm = () => {
  return (
    <div className='wrapper'>
      <form action=''>
        <h1>Login Form</h1>
        <div className='input-box'>
            <input type='text' placeholder='Username' required/>
            <FaUser className='icon'/>
        </div>
        <div className='input-box'>
            <input type='password' placeholder='password' required/>
            <FaLock className='icon'/>
        </div>
        <div className='remember-forgot'>
        <label><input type='checkbox'/>Remember Me</label>
        <a href='#'>Forgot password ?</a>
        </div>
        <button type='submit'>Login</button>
        <div className='register-link'>
            <p>Don't have Account? <a href='#'>Register</a> </p>
        </div>
      </form>
    </div>
  )
}

export default LoginForm
