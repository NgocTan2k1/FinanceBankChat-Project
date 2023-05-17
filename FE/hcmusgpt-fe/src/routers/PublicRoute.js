import { Navigate, Outlet } from 'react-router-dom';
import { isLogin } from '../utils';

const PublicRoute = ({ element: Element, restricted, ...rest }) => {
    const isAuth = isLogin() && restricted;
    return isAuth ? <Navigate to="/chat" /> : <Outlet />;
};

export default PublicRoute;
