import { Navigate, Route, BrowserRouter as Router, Routes } from 'react-router-dom';

import Fobidance404 from './pages/Fobidance404';
import { privateRouters, publicRouters } from './routers';
import PrivateRoute from './routers/PrivateRoute';
import PublicRoute from './routers/PublicRoute';

function App() {
    return (
        <Router>
            <Routes>
                {publicRouters.map((route, index) => {
                    const Page = route.component;
                    return (
                        <Route key={index} path={route.path} element={<PublicRoute restricted={route.restricted} />}>
                            <Route path={route.path} element={<Page />} />
                        </Route>
                    );
                })}

                {privateRouters.map((route, index) => {
                    const Page = route.component;
                    return (
                        <Route key={index} path={route.path} element={<PrivateRoute />}>
                            <Route path={route.path} element={<Page />} />
                        </Route>
                    );
                })}
                <Route path="/404" element={<Fobidance404 />} />
                <Route path="*" element={<Navigate replace to="/404" />} />
            </Routes>
        </Router>
    );
}

export default App;
