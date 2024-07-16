import { createSlice , createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

export const loginUser =createAsyncThunk("login/loginUser" , ({email , password})=>{
    return axios.get("/users/").then((response)=>{
     
    })
})

const loginSlice = createSlice({
    name : "login" ,
    initialState : {
        loading : false ,
        errorMessage : "" , 
        userInfo : {}
    } ,
    reducers : {
        logout : (state , action) => {
            state.userInfo = {}
            localStorage.removeItem("userInfo")
        }
    } ,
    extraReducers : (builder) => {
        builder.addCase(loginUser.pending , (state , action)=>{
            state.loading = true 
            state.errorMessage = ""
            state.userInfo = {}
        })

        builder.addCase(loginUser.fulfilled , (state , action) => {
            state.loading = false 
            state.errorMessage = "" 
            state.userInfo = action.payload
            localStorage.setItem("userInfo" , JSON.stringify(state.userInfo))
        })

        builder.addCase(loginUser.rejected , (state , action) => {
            state.loading = false 
            state.userInfo = {}
            console.log(action)
            state.errorMessage = action.error?.message
        
        })  
    }
})
export default loginSlice.reducer
export const {logout} = loginSlice.actions