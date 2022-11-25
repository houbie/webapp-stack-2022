import React from 'react'
import ReactDOM from 'react-dom/client'
import './App.scss'
import {RouterProvider} from 'react-router-dom';
import {createBrowserRouter} from 'react-router-dom'
import {About} from './About'
import Layout from "./Layout";
import {Home} from "./Home";

const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement)

const router = createBrowserRouter([
    {
        path: "/", element: <Layout/>, children: [
            {index: true, element: <Home/>},
            {path: "about", element: <About/>}
        ]
    }
])

root.render(
    <React.StrictMode>
        <RouterProvider router={router}/>
    </React.StrictMode>
)
