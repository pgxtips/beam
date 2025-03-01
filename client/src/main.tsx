import ReactDOM from 'react-dom/client'
import { BrowserRouter, Routes, Route } from "react-router";

import LoginPage from './pages/login';
import Index from "./pages";
import Settings from "./pages/settings";
import DashLayout from "./pages/dashlayout";

import './import.css';

const root = document.getElementById("root");

ReactDOM.createRoot(root!).render(
<BrowserRouter>
    <Routes>
        <Route path="/dashboard" element={<DashLayout />}>
            <Route index element={<Index/>} />
            <Route path="settings" element={<Settings/>} />
        </Route>
        <Route path="/login" element={<LoginPage/>} />
    </Routes>
</BrowserRouter>
)
